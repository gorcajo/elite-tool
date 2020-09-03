from typing import List

from fpdf import FPDF


# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html


class RepairmentPdf(FPDF):

    def _add_section_header(self, section_name: str):
        title_cell_height = 25

        self.set_fill_color(180, 180, 180)

        self.set_font(family="Arial", style="I", size=15)
        self.cell(w=40, h=title_cell_height, txt=f"[LOGO]", ln=0, align="C", border=True)

        self.set_font(family="Arial", style="B", size=20)
        self.cell(w=110, h=title_cell_height, txt=f"  {section_name}", ln=0, fill=True)

        self.set_font(family="Arial", style="I", size=15)
        self.cell(w=0, h=title_cell_height, txt=f"#{self.repairment['id']} ", ln=1, align="R", fill=True)


    def _add_section_subheader(self):
        cell_height = 4

        self.cell(w=50, h=cell_height, txt="", ln=0)

        self.set_font(family="Arial", style="BI", size=8)
        self.cell(w=16, h=cell_height, txt=f"Domicilio:", ln=0)
        self.set_font(family="Arial", style="I", size=8)
        self.cell(w=35, h=cell_height, txt=f"C/ Peñuelas 25, 28005", ln=0)

        self.set_font(family="Arial", style="BI", size=8)
        self.cell(w=8, h=cell_height, txt=f"Tel.:", ln=0)
        self.set_font(family="Arial", style="I", size=8)
        self.cell(w=35, h=cell_height, txt=f"912328853, 661192909", ln=0)

        self.set_font(family="Arial", style="BI", size=8)
        self.cell(w=9, h=cell_height, txt=f"Mail:", ln=0)
        self.set_font(family="Arial", style="I", size=8)
        self.cell(w=35, h=cell_height, txt=f"info@elitemacpc.com", ln=1)

        self.cell(w=70, h=cell_height, txt="", ln=0)

        self.set_font(family="Arial", style="BI", size=8)
        self.cell(w=18, h=cell_height, txt=f"HORARIO:", ln=0)
        self.set_font(family="Arial", style="I", size=8)
        self.cell(w=0, h=cell_height, txt=f"Lun-Vie: 10:00-14:00 y 17:00-21:00, Sáb: 10:00-14:00", ln=1)

        self.ln(5)


    def _add_section_body(self):
        self._add_highlighted_row(key="Propietario", value=self.repairment["customer_name"])
        self._add_highlighted_row(key="Teléfono móvil", value=self.repairment["customer_phone"])
        self._add_highlighted_row(key="Equipo", value=self.repairment["type"])

        self.ln(5)

        self._add_cell("Fabricante:", self.repairment["manufacturer"])
        self._add_cell("Fecha de recepción:", self.repairment["reception_date"], newline=True)

        self._add_cell("Modelo:", self.repairment["model"])
        estimated_cost = self.repairment["estimated_cost"]
        estimated_cost_str = str(estimated_cost)[:-2] + "." + str(estimated_cost)[-2:] + " EUR"
        self._add_cell("Fecha de retirada:", "TO DO", newline=True)

        self._add_cell("Número de serie:", self.repairment["serial_number"], newline=True)

        self._add_cell("", "", newline=True)

        self._add_cell("Copia de seguridad:", "TO DO")
        self._add_cell("Coste aproximado:", estimated_cost_str, newline=True)

        self._add_cell("Contraseña:", "TO DO", newline=True)

        self.ln(5)

        self._add_multicell("Problema del equipo:", self.repairment["description"])

    
    def _add_highlighted_row(self, key: str, value: str):
        self.set_fill_color(220, 220, 220)

        cell_width = 40
        cell_height = 6

        self.set_font(family="Arial", style="B", size=12)
        self.cell(w=cell_width, h=cell_height, txt=f" {key}", ln=0, fill=True)
        
        self.set_font(family="Arial", style="", size=12)
        self.cell(w=0, h=cell_height, txt=value, ln=1, fill=True)


    def _add_cell(self, key: str, value: str, newline=False):
        margin_cell = 5
        cell_width = 45
        cell_height = 6

        self.cell(w=margin_cell, h=cell_height, txt="", ln=0)

        self.set_font(family="Arial", style="B", size=10)
        self.cell(w=cell_width, h=cell_height, txt=key, ln=0, align="R")
        
        self.set_font(family="Arial", style="", size=10)
        self.cell(w=cell_width, h=cell_height, txt=value, ln=0)

        if newline:
            self.ln(cell_height)


    def _add_multicell(self, key: str, value: str):
        cell_width = 45
        cell_height = 6

        self.set_font(family="Arial", style="B", size=10)
        self.cell(w=cell_width, h=cell_height, txt=key, ln=0, align="R")
        
        self.set_font(family="Arial", style="", size=10)
        self.multi_cell(w=0, h=cell_height, txt=value)


    def set_repairment(self, repairment: dict):
        self.repairment = repairment
        

    def build(self):
        self.add_page()

        self._add_section_header("PRESUPUESTO")
        self._add_section_subheader()
        self._add_section_body()

        while self.get_y() < (self.h / 2):
            self.ln(1)

        self._add_section_header("COPIA DE RESGUARDO")
        self._add_section_subheader()
        self._add_section_body()
