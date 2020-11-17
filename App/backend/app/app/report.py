from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from PIL import Image as pil_image
import io, base64

story = []

styles=getSampleStyleSheet()

center_style = ParagraphStyle('yourtitle',
                        fontName="Courier",
                        fontSize=16,
                        alignment=1,
                        spaceAfter=50)

left_style = ParagraphStyle('yourtitle',
                        fontName="Courier",
                        fontSize=12,
                        alignment=0,
                        spaceAfter=5)

def draw_image(image, height, width):
    I = Image(image)
    I.drawHeight =  height*cm
    I.drawWidth = width*cm

    return I

def generate_report(info, normal_distribution_graph, services_availability_graph, heatmap, bar_plot):
    stream = io.BytesIO()
    doc = SimpleDocTemplate(stream,pagesize=A4)
    story.append(Paragraph('REPORT', center_style))

    information = ['Player: <b>%s</b>' % info[0],
                'Scenario: ' + '<b>%s</b>' % info[1],
                'Scenario level: <b>%s</b>' % info[2],
                'Player\'s level before: <b>%s</b>' % info[3],
                'Player\'s level after: <b>%s</b>' % info[4],
                'Started at: <b>%s</b>' % info[5],
                'Finished at: <b>%s</b>' % info[6]]

    for x in information:
        story.append(Paragraph(x, left_style))

    norm = draw_image(normal_distribution_graph, 10, 14)
    story.append(norm)

    norm_paragraph = 'cnjdncj cnjdnxcjd cxndjnxcujdnxc jcmxjsxcsd dijcxmi djxc dcjidjc dnc djicjmdisjcm sdnjcnds c'
    story.append(Paragraph(norm_paragraph, left_style))

    availability = draw_image(services_availability_graph, 10, 14)
    story.append(availability)

    availability_paragraph = 'cnjdncj cnjdnxcjd cxndjnxcujdnxc jcmxjsxcsd dijcxmi djxc dcjidjc dnc djicjmdisjcm sdnjcnds c'
    story.append(Paragraph(availability_paragraph, left_style))

    heatmap = draw_image(heatmap, 10, 14)
    story.append(heatmap)

    heatmap_paragraph = 'cnjdncj cnjdnxcjd cxndjnxcujdnxc jcmxjsxcsd dijcxmi djxc dcjidjc dnc djicjmdisjcm sdnjcnds c'
    story.append(Paragraph(heatmap_paragraph, left_style))

    bar_plot = draw_image(bar_plot, 10, 14)
    story.append(bar_plot)

    bar_plot_paragraph = 'cnjdncj cnjdnxcjd cxndjnxcujdnxc jcmxjsxcsd dijcxmi djxc dcjidjc dnc djicjmdisjcm sdnjcnds c'
    story.append(Paragraph(bar_plot_paragraph, left_style))

    doc.build(story)
    stream.seek(0)

    return stream
    






def static():

    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    width, height = A4
    file_name = 'abc.pdf'
    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont('Courier', 18)
    c.drawCentredString(10.5*cm, 27.5*cm, 'GAME REPORT')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 26*cm, 'Player: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(5*cm, 26*cm, 'Vardas Pavardauskas')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 25.5*cm, 'Scenario: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(5.5*cm, 25.5*cm, 'SCADA')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 25*cm, 'Scenario level: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(7*cm, 25*cm, 'NAUJOKAS')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 24.5*cm, 'Level before: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(6.5*cm, 24.5*cm, 'NULL')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 24*cm, 'Level after: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(6.35*cm, 24*cm, 'NAUJOKAS')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 23.5*cm, 'Started at: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(6*cm, 23.5*cm, '2020-11-07 11:28:12.493907')

    c.setFont('Courier', 12)
    c.drawString(3*cm, 23*cm, 'Finished at: ')
    c.setFont('Courier-Bold', 12)
    c.drawString(6.35*cm, 23*cm, '2020-11-07 11:28:17.453000')

    norm = ImageReader('normal.jpeg')
    c.drawImage(norm, 6*cm, 15*cm, width=10*cm, height=8*cm, mask='auto')

    P = Paragraph('tekstas tekstas csj xunds xnds xjndsjixuh ', styleN)
    c.showPage()
    c.save()