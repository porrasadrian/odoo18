# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    related_invoice_names = fields.Char(
        string="Facturas relacionadas",
        compute="_compute_related_invoice_names",
        readonly=True,
    )

    @api.depends('related_invoice_ids')
    def _compute_related_invoice_names(self):
        for line in self:
            names = []
            for inv in line.related_invoice_ids:
                name = "{} / {} / {}".format(
                    inv.number or '',
                    inv.journal_id.name or '',
                    inv.date_invoice or ''
                )
                names.append(name)
            line.related_invoice_names = ', '.join(names) if names else ''

    related_invoice_ids = fields.Many2many(
        'account.invoice',
        string='Facturas relacionadas',
        readonly=True,
    )
    #FUNCION PRINCIPAL
    @api.multi
    def relate_invoice(self):
        for line in self:
            if not line.account_id or line.account_id.code != '208.01.01':
                continue
            if not line.journal_id or line.journal_id.type != 'bank':
                continue

            invoice_ids = set()

            for related_line in line.move_id.line_ids:
                if related_line.account_id.code == '105.01.05' and related_line.related_invoice_ids:
                    for inv in related_line.related_invoice_ids:
                        invoice_ids.add(inv.id)
                    break

            if not invoice_ids:
                for related_line in line.move_id.line_ids:
                    if related_line.account_id.code == '105.01.05' and related_line.full_reconcile_id:
                        for rec_line in related_line.full_reconcile_id.reconciled_line_ids:
                            move = rec_line.move_id
                            journal = rec_line.journal_id
                            move_name = move.name or ''
                            journal_name = journal.name if journal else ''

                            if journal_name == 'Factura de cliente' or move_name.startswith('F0'):
                                invoice = self.env['account.invoice'].search([('move_id', '=', move.id)], limit=1)
                                if invoice:
                                    invoice_ids.add(invoice.id)

            if invoice_ids:
                line.write({'related_invoice_ids': [(6, 0, list(invoice_ids))]})


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def name_get(self):
        result = []
        for inv in self:
            name = "{} / {} / {}".format(
                inv.number or '',
                inv.journal_id.name or '',
                inv.date_invoice or ''
            )
            result.append((inv.id, name))
        return result
