from .models import MAWB


def mawb_dict_for_frontend(request, id: int):
    mawb = MAWB.objects.get(id=id)
    shipper_address = mawb.shipper
    consignee_address = mawb.consignee
    formdata = {
        'mawb_reference_number': mawb.public_id,
        'shipper_name': shipper_address.company_name if shipper_address else '',
        'shipper_address': shipper_address.address if shipper_address else '',
        'shipper_po_code': shipper_address.postcode if shipper_address else '',
        'shipper_city': shipper_address.city.id if shipper_address else '',
        'shipper_state': shipper_address.state if shipper_address else '',
        'shipper_country': shipper_address.country.id if shipper_address else '',
        'shipper_contact': shipper_address.contact if shipper_address else '',
        'shipper_tel_number': shipper_address.phone if shipper_address else '',
        'shipper_mob_num': shipper_address.mobile if shipper_address else '',
        'shipper_fax_num': shipper_address.fax if shipper_address else '',
        'shipper_email': shipper_address.email if shipper_address else '',
        'shipper_acc_no': '',
        'consignee_name': consignee_address.company_name if consignee_address else '',
        'consignee_address': consignee_address.address if consignee_address else '',
        'consignee_po_code': consignee_address.postcode if consignee_address else '',
        'consignee_city': consignee_address.city.id if consignee_address else '',
        'consignee_state': consignee_address.state if consignee_address else '',
        'consignee_country': consignee_address.country.id if consignee_address else '',
        'consignee_contact': consignee_address.contact if consignee_address else '',
        'consignee_tel_number': consignee_address.phone if consignee_address else '',
        'consignee_mob_num': consignee_address.mobile if consignee_address else '',
        'consignee_fax_num': consignee_address.fax if consignee_address else '',
        'consignee_email': consignee_address.email if consignee_address else '',
        'consignee_acc_no': '',

        'carrier_agent_name': mawb.carrier_agent_name,
        'carrier_agent_city': mawb.carrier_agent_city_id,
        'carrier_agent_state': mawb.carrier_agent_state,
        'carrier_agent_country': mawb.carrier_agent_country_id,
        'carrier_agent_ffl': mawb.carrier_agent_ffl_no,
        'carrier_agent_date': mawb.carrier_agent_date.strftime('%Y-%m-%d') if mawb.carrier_agent_date else '',
        'carrier_agent_iata_code': mawb.carrier_agent_iata_code,
        'carrier_agent_acc_no': mawb.carrier_agent_account_no,

        'payment_type': mawb.payment_type_id,
        'departure_airport': mawb.airport_of_departure_id,
        'requested_routing': mawb.requested_routing,
        'destination_to_1_airport': mawb.to_1_airport_id,
        'destination_to_1_airline': mawb.to_1_airline_id,
        'destination_to_1_flight_num': mawb.to_1_flight_num,
        'destination_to_1_flight_date': mawb.to_1_flight_date.strftime('%Y-%m-%d') if mawb.to_1_flight_date else '',
        'destination_to_2_airport': mawb.to_2_airport_id,
        'destination_by_2_airline': mawb.to_2_airline_id,
        'destination_to_2_flight_num': mawb.to_2_flight_num,
        'destination_to_2_flight_date': mawb.to_2_flight_date.strftime('%Y-%m-%d') if mawb.to_2_flight_date else '',
        'destination_to_3_airport': mawb.to_3_airport_id,
        'destination_to_3_airline': mawb.to_3_airline_id,
        'destination_to_3_flight_num': mawb.to_3_flight_num,
        'destination_to_3_flight_date': mawb.to_3_flight_date.strftime('%Y-%m-%d') if mawb.to_3_flight_date else '',
        'dest_airport': mawb.airport_of_destination_id,
        'requested_flight_date': '',
        'reff_no_1': '',
        'reff_no_2': '',
        'reff_no_3': '',
        'currency': mawb.currency_id,
        'cngs_code': mawb.cngs_code,
        'wt': mawb.wt_val_payment_type_id,
        'other_wt': mawb.other_payment_type_id,
        'carriage_value': mawb.declared_val_for_carriage,
        'customs_value': mawb.declared_val_for_customs,
        'insurance_amount': mawb.amt_of_insurance,
        'handling_info': mawb.handling_info,
        'goods_no_piece_rcp': mawb.goods_noofpcsrcp,
        'goods_gross_weight': mawb.goods_grossweight,
        'goods_weight_unit': mawb.goods_weightunit,
        'goods_commodity_item_no': mawb.goods_commodityitemno,
        'goods_chargeable_weight': mawb.goods_chargableweight,
        'goods_rate': mawb.goods_ratecharge,
        'goods_total': mawb.goods_total,
        'goods_nature': mawb.goods_natureandquantity,
        'weightcharge_prepaid': mawb.weightcharge_prepaid,
        'weightcharge_collect': mawb.weightcharge_collect,
        'others_valuation_prepaid': mawb.valuationcharge_prepaid,
        'others_valuation_collect': mawb.valuationcharge_collect,
        'others_tax_prepaid': mawb.tax_prepaid,
        'others_tax_collect': mawb.tax_collect,
        'others_cda_prepaid': mawb.totalotherchargesdueagent_prepaid,
        'others_cda_collect': mawb.totalotherchargesdueagent_collect,
        'others_cdc_prepaid': mawb.totalotherchargesduecarrier_prepaid,
        'others_cdc_collect': mawb.totalotherchargesduecarrier_collect,
        'others_total_prepaid': mawb.total_prepaid,
        'others_total_collect': mawb.total_collect,
        'others_ccr': mawb.currencyconversionrate,
        'others_ccc_dest': mawb.ccchargesindestcurrency,
        'others_cad': mawb.chargesatdestination_collect,
        'others_tcc': mawb.totalcharges_collect,
        'others_charges': mawb.charges_other,
        'others_ex_date': mawb.executed_on_date.strftime('%Y-%m-%d') if mawb.executed_on_date else '',
        'others_ex_loc': mawb.executed_at_city_id,
        'others_signature': mawb.signature_shipperoragent,
        'others_sic': mawb.signature_issuingcarrieroragent,
    }
    return formdata