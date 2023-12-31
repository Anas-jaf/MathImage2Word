import xml.etree.ElementTree as ET
import win32com.client as win32
from PIL import Image
import tempfile
import win32gui
import base64
import io
import os
import socket
from docx import Document

def get_all_pictures_in_docx(docx_path):
    doc = Document(docx_path)
    # print([(item , doc.inline_shapes._parent._rels[item].target_part.blob ) for item in doc.inline_shapes._parent._rels])
    blip_data = {}
    idx = 0
    for item in doc.inline_shapes._parent._rels :
        if 'media' in doc.inline_shapes._parent._rels[item].target_ref :
            idx += 1
            target_part = doc.inline_shapes._parent._rels[item].target_part
            blob = target_part.blob
            # blip_data ((item, blob))
            blip_data[idx] = blob
    return blip_data

def get_local_ip_address():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def extract_all_blip_ids(xml_content):
    # Namespace dictionary
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Find all a:blip elements
    blip_elements = root.findall('.//a:blip', namespaces=ns)

    blip_ids = []

    for blip_element in blip_elements:
        r_embed = blip_element.attrib.get(f"{{{ns['r']}}}embed")
        if r_embed:
            blip_ids.append(r_embed)

    return blip_ids

def convert_images_to_latex(image):
    pass
    # pictures = []
    # if doc:
    #     for shape in doc.InlineShapes:
    #         if shape.Type == 3:  # 3 represents pictures
    #             picture_path = os.path.join(os.getcwd(), f"picture_{len(pictures)+1}.jpg")
    #             shape.Range.CopyAsPicture()
    #             word_app = doc.Application
    #             word_app.Selection.Paste()
    #             picture = word_app.ActiveWindow.Selection.ShapeRange[1]
    #             picture.Copy()
    #             picture.Export(picture_path)
    #             pictures.append(picture_path)
    #             word_app.ActiveWindow.Selection.Delete()  # Delete the floating shape from the document
    # return pictures

def set_foreground_window(hwnd):
    try:
        win32gui.SetForegroundWindow(hwnd)
    except Exception as e:
        print("Error:", e)

def is_word_window(hwnd, title):
    try:
        window_title = win32gui.GetWindowText(hwnd)
        return title in window_title
    except Exception:
        return False

def find_word_window(title):
    try:
        hwnd_list = []
        win32gui.EnumWindows(lambda hwnd, hwnd_list: hwnd_list.append(hwnd) if is_word_window(hwnd, title) else None, hwnd_list)
        return hwnd_list[0] if hwnd_list else None
    except Exception as e:
        print("Error:", e)
        return None

def open_word():
    try:
        word = win32.dynamic.Dispatch("Word.Application")
        word.Visible = True
        hwnd = win32gui.FindWindow(None, "Microsoft Word")  # Assuming the window title is "Microsoft Word"
        hwnd = find_word_window("Microsoft Word")  # Try to find the Word window by title
        if hwnd:
            set_foreground_window(hwnd)  # Bring the Word window to the front       
        return word
    except Exception as e:
        print("Error:", e)
        return None

def open_document(word_app):
    try:
        doc = word_app.ActiveDocument
        return doc
    except Exception as e:
        print("Error:", e)
        return None

def insert_image(word_app , decoded_image, image_path=None):
    if word_app:
        try:
            # Get the selection object
            selection = word_app.Selection
            if not decoded_image :
                # Ask the user to provide the image path
                image_path = input("Enter the path to your image: ") if not image_path else image_path
                # Insert the image at the current cursor position
                selection.InlineShapes.AddPicture(FileName=image_path)
            else:
                image_binary = base64.b64decode(decoded_image)
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                    temp_file.write(image_binary)
                    image_path = temp_file.name                
                inline_shape = selection.InlineShapes.AddPicture(FileName=image_path, LinkToFile=False, SaveWithDocument=True)
                image = Image.open(image_path)
                inline_shape.Width = image.width
                inline_shape.Height = image.height                
            for _ in range(2):
                selection.TypeParagraph()
        except Exception as e:
            print("Error:", e)

def create_new_document(word_app):
    doc = open_document(word_app)
    if doc is None:
        # Create a new document if none is open
        doc = word_app.Documents.Add()
    return doc

def open_document_from_path( file_path=None , _word_app=None  ): # note: file_path should be a r string
    try:
        if file_path:
            doc = _word_app.Documents.Open(file_path)
            return doc
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    word_app = open_word()
    # path = r'{}'.format(input("give me word document path"))
    path = r"C:\Users\ansas\OneDrive\Documents\تجربة.docx"
    doc = open_document_from_path(file_path= path , _word_app = word_app)
    convert_images_to_latex(doc)