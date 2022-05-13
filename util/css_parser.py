def css_parser(css_style : str) -> dict[str,float]:
    # style 요소들에 대해 숫자 정보만 파싱해서 가져오는 함수
    styles = css_style.split(';')
    result_dict = {}    
    for style in styles:
        if len(style) > 0:
            style_name, style_val = [ x.strip(' ').replace("px","") for x in style.split(':')]
            style_val = float(style_val)

            result_dict[style_name] = style_val

    return result_dict
    