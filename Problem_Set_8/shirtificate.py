from fpdf import FPDF


name = input("Name: ")

pdf = FPDF()

pdf.add_page()

pdf.set_font("courier", "B", 48)

pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

pdf.image("shirtificate.png", w=pdf.epw)

pdf.set_font_size(28)

pdf.set_text_color(255, 255, 255)

pdf.text(x=50, y=150, text=f"{name} took CS50")

pdf.set_line_width(0.75)

pdf.set_draw_color(0, 0, 0)

pdf.rect(47.5, 139.5, 118, 15.5, round_corners=True, style="D")

pdf.set_draw_color(255, 255, 255)

pdf.rect(48, 140, 117, 14.5, round_corners=True, style="D")

pdf.output("shirtificate.pdf")
