from typing import Dict


def css_parser(css_style : str) -> Dict[str,float]:
    styles = css_style.split(';')
    result_dict = {}    
    for style in styles:
        if len(style) > 0:
            style_name, style_val = [ x.strip(' ').replace("px","") for x in style.split(':')]
            style_val = float(style_val)

            result_dict[style_name] = style_val

    return result_dict
    