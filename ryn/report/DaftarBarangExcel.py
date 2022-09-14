from odoo import models, fields, api

class PartnerXlsx(models.AbstractModel):
    _name = 'report.ryn.report_barang_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Barang')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Nama Barang')
        sheet.write(0, 1, 'Harga Modal')
        sheet.write(0, 2, 'Harga Jual')
        sheet.write(0, 3, 'Stok')
        sheet.write(0, 4, 'Kelompok Barang')
        sheet.write(0, 5, 'Supplier')
        row = 1
        col = 0
        for obj in barang:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, str(obj.harga_beli))
            sheet.write(row, col+2, str(obj.harga_jual))
            sheet.write(row, col+3, str(obj.stok))
            for xxx in obj.kelompokbarang_id:
                sheet.write(row, col+4, xxx.name)
                for yyy in obj.supplier_id:
                    sheet.write(row, col+5, yyy.name)
                    col += 1
            row += 1