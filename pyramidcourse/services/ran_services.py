class RanService:
    @staticmethod
    def get_ran_nodes():
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
