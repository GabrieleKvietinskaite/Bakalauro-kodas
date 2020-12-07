from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus.tables import TableStyle
from reportlab.lib import colors

from PIL import Image as pil_image
import io, base64

story = []

styles=getSampleStyleSheet()

center_style = ParagraphStyle('yourtitle',
                        fontName="Courier",
                        fontSize=16,
                        alignment=1,
                        spaceAfter=25)

left_style = ParagraphStyle('yourtitle',
                        fontName="Courier",
                        fontSize=12,
                        alignment=0,
                        spaceAfter=5)

formula_style = ParagraphStyle('yourtitle',
                        fontName="Times-BoldItalic",
                        fontSize=15,
                        alignment=1,
                        spaceAfter=15, spaceBefore=15)

table_style = ParagraphStyle('yourtitle',
                        fontName="Courier",
                        fontSize=15,
                        alignment=1,
                        spaceAfter=15, spaceBefore=15)

def addPageNumber(canvas, doc):
    page_num = canvas.getPageNumber()
    canvas.drawRightString(20*cm, 2*cm, str(page_num))

def draw_image(image, height, width):
    I = Image(image)
    I.drawHeight =  height*cm
    I.drawWidth = width*cm

    return I

def generate_report(info, normal_distribution_graph, services_availability_graph, best_path, bar_plot, htmap, scoring):
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

    story.append(Paragraph('', formula_style))

    data1= [['CATEGORY', 'SCORE', 'WEIGHT'],
    ['AVAILABILITY (A)', scoring[0], '45%'],
    ['DEFENCE (D)', scoring[1], '20%'],
    ['REPORTS (R)', scoring[2], '20%'],
    ['BUSINESS (B)', scoring[3], '10%'],
    ['OTHER (O)', scoring[4], '5%'],
    ['TOTAL OF SCORE:', scoring[5], '100%'],]

    t=Table(data1)
    t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

    story.append(t)
    score_formula = 'SCORE = 45% * A + 20% * D + 20% * R + 10% * B + 5% * O'
    story.append(Paragraph(score_formula, formula_style))

    norm = draw_image(normal_distribution_graph, 10, 14)
    story.append(norm)

    norm_paragraph = 'This is normal distribution N(μx; σx) graph. This graph shows the distribution of results among players of the same level. The red dot indicates where You are based on your collected points.'
    story.append(Paragraph(norm_paragraph, left_style))

    availability = draw_image(services_availability_graph, 10, 14)
    story.append(availability)

    availability_paragraph = 'It is a linear graph showing how the availability of services has changed according to your choices.'
    story.append(Paragraph(availability_paragraph, left_style))

    best_path = draw_image(best_path, 10, 14)
    story.append(best_path)

    best_path_paragraph = 'This is a linear graph showing how many points you got per question (orange line) and what maximum number of points you could score (blue line).'
    story.append(Paragraph(best_path_paragraph, left_style))

    bar_plot = draw_image(bar_plot, 10, 14)
    story.append(bar_plot)

    bar_plot_paragraph = 'This bar graph shows how many players have reached what level: novice, proficient, advanced, professional or expert.'
    story.append(Paragraph(bar_plot_paragraph, left_style))

    htmap = draw_image(htmap, 10, 14)
    story.append(htmap)

    htmap_paragraph = 'This heat map shows the frequency of answers to all the questions depicted in the game. The darker the color, the more times this answer option was chosen in the question. At least one box can be noticed for each question, where the number of answer choices is circled. This means that this is the answer you have chosen.'
    story.append(Paragraph(htmap_paragraph, left_style))

    doc.build(story, onFirstPage=addPageNumber, onLaterPages=addPageNumber)
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