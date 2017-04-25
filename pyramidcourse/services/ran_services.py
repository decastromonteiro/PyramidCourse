class RANService:
    @staticmethod
    def get_utran_info(rnc_name, sgsn_name, plmn, mcc, mnc, lac, rnc_id):
        return [

            {'name': 'ARJO01',
             'type': 'RNC',
             'core_node': ['DMRJO4', 'DMRJO3'],
             'plmn': '72402',
             'mcc': '724',
             'mnc': '02'},

            {'name': 'ASPO01',
             'type': 'RNC',
             'core_node': ['DMSNE3', 'DMSNE4', 'DMSPO2', 'DMSPO1'],
             'plmn': '72403',
             'mcc': '724',
             'mnc': '03'}
        ]

    @staticmethod
    def get_geran_info(bsc_name, sgsn_name, nsei, lac, plmn, mcc, mnc):
        return [

            {'name': 'BRJO01',
             'type': 'RNC',
             'core_node': ['DMRJO4', 'DMRJO3'],
             'plmn': '72402',
             'mcc': '724',
             'mnc': '02'},

            {'name': 'BSPO01',
             'type': 'RNC',
             'core_node': ['DMSNE3', 'DMSNE4', 'DMSPO2', 'DMSPO1'],
             'plmn': '72403',
             'mcc': '724',
             'mnc': '03'}
        ]

    @staticmethod
    def get_eutran_info(tac, lac, vlr_name, vlr_number):
        return [

            {'name': 'ARJO01',
             'type': 'RNC',
             'core_node': ['DMRJO4', 'DMRJO3'],
             'plmn': '72402',
             'mcc': '724',
             'mnc': '02'},

            {'name': 'ASPO01',
             'type': 'RNC',
             'core_node': ['DMSNE3', 'DMSNE4', 'DMSPO2', 'DMSPO1'],
             'plmn': '72403',
             'mcc': '724',
             'mnc': '03'}
        ]
