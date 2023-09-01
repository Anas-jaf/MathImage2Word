import requests
import json 
from requests_toolbelt.multipart.encoder import MultipartEncoder

def dict_to_equation(node):
    if "children" in node:
        children = node["children"]
        left_child = dict_to_equation(children[0])
        
        if len(children) > 1:  # Check if there's a right child
            right_child = dict_to_equation(children[1])
            if len(children) > 2:
                last_child = dict_to_equation(children[2])
            # children = [dict_to_equation(child) for child in node["children"]] 
        
        if node["type"] == "add":
            return f"{left_child} + {right_child}"
        elif node["type"] == "sub":
            return f"{left_child} - {right_child}"
        elif node["type"] == "mul":
            return f"{left_child} \\times {right_child}"
        elif node["type"] == "div":
            return f"{left_child} \\div {right_child}"
        elif node["type"] == "frac":
            return "\\frac{"+f"{left_child}" + "}{" f"{right_child}" +"}"
        elif node["type"] == "pow":
            return f"{left_child} ^ {right_child}"
        elif node["type"] == "endequals":
            return f"{left_child} ="
        elif node["type"] == "negative":
            return f"-{left_child}"
        elif node["type"] == "bracket":
            return f"({left_child})"
        elif node["type"] == "gt":
            return f"{left_child} > {right_child}" 
        elif node["type"] == "gte":
            return f"{left_child} \geq {right_child}"
        elif node["type"] == "lt":
            return f"{left_child} < {right_child}"
        elif node["type"] == "lte":
            return f"{left_child} \leq {right_child}"    
        elif node["type"] == "percentage":
            return f"{left_child}%"
        elif node["type"] == "muli":
            return f"{left_child} \\cdot {right_child}"        
        elif node["type"] == "mixedfrac":
            return f"{left_child}" + "\\frac{" + f"{dict_to_equation(children[1])}" + "}{" + f"{dict_to_equation(children[2])}" + "}"
        elif node["type"] == "abs":
            return f"\\left|{left_child}\\right|"
        elif node["type"] == "exp":
            return f"\\exp({left_child})"
        elif node["type"] == "function":
            if len(children) > 2 : 
                return f"\\mathrm{{{left_child}}}(\\mathrm{{{right_child}}} , \\mathrm{{{last_child}}})"
            else :
                return f"\\mathrm{{{left_child}}}(\\mathrm{{{right_child}}})"
        elif node["type"] == "equals":
            return f"{left_child} = {right_child}"
        elif node["type"] == "log":
            return f"\\log_{{{left_child}}} ({{{right_child}}})"
        elif node["type"] == "ln":
            return f"\\ln({left_child})"        
        elif node["type"] == "conj":
            return f"\\overline{{{left_child}}}"        
        elif node["type"] == "sign":
            return f"\\text{{sign}}({left_child})"            
        elif node["type"] == "mixedfrac":
            whole = dict_to_equation(node["children"][0])
            numerator = dict_to_equation(node["children"][1])
            denominator = dict_to_equation(node["children"][2])
            return f"{whole} \\frac{{{numerator}}}{{{denominator}}}"
        elif node["type"] == "factorial":
            return f"{left_child}!"  
        elif node["type"] == "radian":
            return f"{left_child} \\, \\text{{rad}}"
        elif node["type"] == "deg":
            return f"{left_child} \\degree"
        elif node["type"] == "degmin":
            deg_child = dict_to_equation(node["children"][0])
            min_child = dict_to_equation(node["children"][1])
            return f"{deg_child}° {min_child}'"
        elif node["type"] == "degminsecond":
            deg_child = dict_to_equation(node["children"][0])
            min_child = dict_to_equation(node["children"][1])
            sec_child = dict_to_equation(node["children"][2])
            return f"{deg_child}° {min_child}' {sec_child}''"
        elif node["type"] == "sin":
            return f"\\sin({left_child})"
        elif node["type"] == "asin":
            return f"\\arcsin({left_child})"
        elif node["type"] == "sinh":
            return f"\\sinh({left_child})"  
        elif node["type"] == "asinh":
            return f"\\\\arsinh({left_child})"
        
        elif node["type"] == "cos":
            return f"\\cos({left_child})"
        elif node["type"] == "acos":
            return f"\\arccos({left_child})"
        elif node["type"] == "cosh":
            return f"\\cosh({left_child})"  
        elif node["type"] == "acosh":
            return f"\\\\arcosh({left_child})"

        elif node["type"] == "cos":
            return f"\\cos({left_child})"
        elif node["type"] == "acos":
            return f"\\arccos({left_child})"
        elif node["type"] == "cosh":
            return f"\\cosh({left_child})"  
        elif node["type"] == "acosh":
            return f"\\\\arcosh({left_child})"
        
        elif node["type"] == "tan":
            return f"\\tan({left_child})"
        elif node["type"] == "atan":
            return f"\\arctan({left_child})"
        elif node["type"] == "tanh":
            return f"\\tanh({left_child})"  
        elif node["type"] == "atanh":
            return f"\\\\artanh({left_child})"        
                        
        elif node["type"] == "cot":
            return f"\\cot({left_child})"
        elif node["type"] == "acot":
            return f"\\arccot({left_child})"
        elif node["type"] == "coth":
            return f"\\coth({left_child})"  
        elif node["type"] == "acoth":
            return f"\\\\arcoth({left_child})"                           

        elif node["type"] == "sec":
            return f"\\sec({left_child})"
        elif node["type"] == "asec":
            return f"\\arcsec({left_child})"
        elif node["type"] == "sech":
            return f"\\sech({left_child})"  
        elif node["type"] == "asech":
            return f"\\\\arsech({left_child})" 

        elif node["type"] == "csc":
            return f"\\csc({left_child})"
        elif node["type"] == "acsc":
            return f"\\arccsc({left_child})"
        elif node["type"] == "csch":
            return f"\\csch({left_child})"  
        elif node["type"] == "acsch":
            return f"\\\\arcsch({left_child})" 

        elif node["type"] == "lim":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}}} ({function_child})"

        elif node["type"] == "lim_right":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}^+}} ({function_child})"
        
        elif node["type"] == "lim_left":
            var_child = dict_to_equation(node["children"][0])
            lower_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\lim_{{ {var_child} \\to {lower_child}^-}} ({function_child})"
        
        elif node["type"] == "derivation":                
            var_child = dict_to_equation(node["children"][0])
            function_child = dict_to_equation(node["children"][1])
            # if len(children) > 2:
            return f"\\frac{{\\mathrm{{d}}}}{{\\mathrm{{d}}{var_child}}}{{({function_child})}}"
        
        elif node["type"] == "nderivation":
            pow_child = dict_to_equation(node["children"][0])
            var_child = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            return f"\\frac{{d^{{{pow_child}}}}}{{d{var_child}^{{{pow_child}}}}}{{{function_child}}}"
            
        elif node["type"] == "integral":
            function_child = dict_to_equation(node["children"][0])
            var_child = dict_to_equation(node["children"][1])            
            return f"\\int {function_child} d{var_child}"

        elif node["type"] == "definiteintegral":
            lower_limit = dict_to_equation(node["children"][0])
            upper_limit = dict_to_equation(node["children"][1])
            function_child = dict_to_equation(node["children"][2])
            var_child = dict_to_equation(node["children"][3])
            return  f"\\int_{{{lower_limit}}}^{{{upper_limit}}} {function_child} d{var_child}"
        
        elif node["type"] == "definitesigma":
            var_child = dict_to_equation(node["children"][0])
            start_child = dict_to_equation(node["children"][1])
            end_child = dict_to_equation(node["children"][2])
            function_child = dict_to_equation(node["children"][3])
            return f"\\sum_{{{var_child}={start_child}}}^{{{end_child}}} ({function_child})"

        elif node["type"] == "derivation_diff":
            var_child1 = dict_to_equation(node["children"][0])
            var_child2 = dict_to_equation(node["children"][1])
            return f"\\frac{{\\mathrm{{d}}{var_child2}}}{{\\mathrm{{d}}{var_child1}}}"
        
        elif node["type"] == "differential":
            var_child = dict_to_equation(node["children"][0])
            return f"\\mathrm{{d}}{var_child}"
            
        elif node["type"] == "derivationprime":
            var_child = dict_to_equation(node["children"][0])
            return f"{{{var_child}}}^{{\\prime}}"

        elif node["type"] == "choose":
            left_value = dict_to_equation(node["children"][0])
            right_value = dict_to_equation(node["children"][1])
            return f"{{{{{left_value}}} \\choose {{{right_value}}}}}"

    elif node["type"] == "const":
        return node["value"]
    elif node["type"] == "var":
        if node["value"] == 'π':
          return '\pi'
        elif node["value"] == 'e':
          return '\mathrm{e}' 
        elif node["value"] == '∞':
            return '\infty'
        return node["value"]
    elif node["type"] == "ellipsis":
        return "..."
    
def image_ocr_photomath(auth , image_path=None , image_content=None):
    burp0_url = "https://pws.photomath.net:443/v5/process-image-groups?bookpoint=false&problemdb=true&locale=en&locale_allow_missing=false&check_solution=false&multipart=true&documents=true"
    burp0_headers = {
            "User-Agent": "Photomath/8.28.0 (Android 9; en; SM-G977N; Build/LMY48Z)",
            "Authorization": f"Bearer {auth}",
            "Accept-Encoding": "gzip, deflate"
            }

    # Create the 'json' part as a dictionary
    json_data = {
        "view": {
                 "height": 200,
                 "width": 700,
                 "x": 0,
                 "y": 0
                },
        "metadata": {
                     "appLanguage": "en",
                     "appVersion": "8.28.0-936",
                     "debug": False, "device": "samsung - SM-G977N",
                     "eventType": "gallery", "imageCollectionOptOut": False,
                     "location": "JO-AM",
                     "osVersion": "9",
                     "platform": "ANDROID",
                     "scanCounter": 0,
                     "scanId": "gallery-09bdef3c-49ab-4c6b-b04b-5f53d9ec0192",
                     "sessionId": "crop-a1fe1f9823024647932bf3acc992e4b0"
                    },
        "experiments": {
                        "spanishMonetization": "Variant2",
                        "italianMonetization": "Variant1",
                        "portugueseMonetization": "false",
                        "inlineAnimations": "Variant1"
                        },
        "animatedPreview": True
    }

    # Serialize the dictionary to JSON and encode it as bytes
    json_bytes = json.dumps(json_data).encode('utf-8')
    
    if not image_content :
        image_content = open(image_path , 'rb')

    # Create a multipart encoder with auto-generated boundary
    multipart_encoder = MultipartEncoder(
        fields={
            'image': ('Untitled3.jpg', image_content , 'application/octet-stream'),
            'json': ('json', json_bytes, 'application/json')
        }
    )

    burp0_headers['Content-Type'] = multipart_encoder.content_type

    proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

    response = requests.post(burp0_url, headers=burp0_headers, data=multipart_encoder, proxies=proxies, verify=False)

    json_data = response.json()
    
    return json_data
    # return json_data['result']['groups'][0]['entries'][0]['nodeAction']['node']
    


















    