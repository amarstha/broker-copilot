# from io import BytesIO
# from django.template.loader import get_template
# # from xhtml2pdf import pisa

# def html_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if pdf.err:
#         return None
#     return result.getvalue()

