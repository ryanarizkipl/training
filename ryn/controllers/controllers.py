from odoo import http, models, fields
from odoo.http import request
import json

class Ryn(http.Controller):
    @http.route('/ryn/getbarang', auth='public', method=['GET'])
    def getBarang (self, **kw):
        barang = request.env['ryn.barang'].search([])
        isi = []
        for bb in barang:
            isi.append ({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)
    
    @http.route('/ryn/getsupplier', auth='public', method=['GET'])
    def getSupplier (self, **kw):
        supplier = request.env['ryn.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append ({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telp' : s.no_telp
            })
        return json.dumps(sup)
