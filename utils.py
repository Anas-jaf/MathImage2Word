import base64
import io
import tempfile
import win32com.client as win32
from PIL import Image

def open_word():
    try:
        word = win32.gencache.EnsureDispatch("Word.Application")
        word.Visible = True
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

def get_or_create_document(word_app):
    doc = open_document(word_app)
    if doc is None:
        # Create a new document if none is open
        doc = word_app.Documents.Add()
    return doc

if __name__ == "__main__":
    word_app = open_word()
    
    get_or_create_document(word_app)
    while True:
        insert_image(word_app)