from enum import Enum
class AcronymCatalogs(object):
    # acqDict = {'3': 'Impl', '4': 'Impl', '130': 'Impl', '131': 'Impl',
    #            '6': 'Prp', '7': 'Prp',
    #            '8': 'Dnt', '9': 'Dnt', '140': 'Dnt', '141': 'Dnt',
    #            '200': 'Ext', '201': 'Ext', '202': 'Ext',
    #            '21': 'Impr', '22': 'Impr', '23': 'Impr', '31': 'Impr', '32': 'Impr', '33': 'Impr',
    #            '41': 'PrpImpr', '42': 'PrpImpr', '43': 'PrpImpr', '51': 'PrpImpr', '52': 'PrpImpr', '53': 'PrpImpr',
    #            '61': 'ImplImpr', '62': 'ImplImpr', '63': 'ImplImpr', '71': 'ImplImpr', '72': 'ImplImpr', '73': 'ImplImpr',
    #            '81': 'DntImpr', '82': 'DntImpr', '83': 'DntImpr', '91': 'DntImpr', '92': 'DntImpr', '93': 'DntImpr'}
    acqDict = {'3': 'Impl', '4': 'Impl', '130': 'Impl', '131': 'Impl',
               '6': 'Prp', '7': 'Prp',
               '8': 'Dnt', '9': 'Dnt', '140': 'Dnt', '141': 'Dnt',
               '200': 'Ext', '201': 'Ext', '202': 'Ext',
               '21': 'Impr', '22': 'Impr', '23': 'Impr', '31': 'Impr', '32': 'Impr', '33': 'Impr',
               '41': 'Impr', '42': 'Impr', '43': 'Impr', '51': 'Impr', '52': 'Impr', '53': 'Impr',
               '61': 'Impr', '62': 'Impr', '63': 'Impr', '71': 'Impr', '72': 'Impr', '73': 'Impr',
               '81': 'Impr', '82': 'Impr', '83': 'Impr', '91': 'Impr', '92': 'Impr', '93': 'Impr',
               '100':'Exb','101':'Exb','102':'Exb','103':'Exb','104':'Exb','105':'Exb','106':'Exb','107':'Exb','108':'Exb','109':'Exb',
               '110':'Exb','111':'Exb','112':'Exb','113':'Exb','114':'Exb','115':'Exb','116':'Exb','117':'Exb','118':'Exb','119':'Exb',
               '120':'Exb','121':'Exb','122':'Exb','123':'Exb'}
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=object.__new__(cls)
        return cls._instance
    def __init__(self):
        pass

    @classmethod
    def acqCatalogs(self):
        return self.acqDict


class CatalogIds(Enum):
    UNKNOWN_JAW = -2,#error flag
    ANY_JAW = -1,#algo use
    LOWER_JAWER = 0,
    UPPER_JAWER = 1,
    BUCCAL = 2,
    LOWER_JAWER_IMPLANT = 3,
    UPPER_JAWER_IMPLANT = 4,
    BUCCAL_CAPTURING = 5,
    LOWER_JAWER_DUAL = 6,
    UPPER_JAWER_DUAL = 7,
    LOWER_EDENTULOUS = 8,
    UPPER_EDENTULOUS = 9,

    BITE_1 = 11,
    BITE_2 = 12,
    BITE_3 = 13,
    BITE_4 = 14,
    BITE_5 = 15,
    BITE_6 = 16,

    LOWER_IMPRESSION_1 = 21,
    LOWER_IMPRESSION_2 = 22,
    LOWER_IMPRESSION_3 = 23,

    UPPER_IMPRESSION_1 = 31,
    UPPER_IMPRESSION_2 = 32,
    UPPER_IMPRESSION_3 = 33,

    LOWER_POSTSCAN_IMPRESSION_1 = 41,
    LOWER_POSTSCAN_IMPRESSION_2 = 42,
    LOWER_POSTSCAN_IMPRESSION_3 = 43,

    UPPER_POSTSCAN_IMPRESSION_1 = 51,
    UPPER_POSTSCAN_IMPRESSION_2 = 52,
    UPPER_POSTSCAN_IMPRESSION_3 = 53,

    LOWER_IMPLANT_IMPRESSION_1 = 61,
    LOWER_IMPLANT_IMPRESSION_2 = 62,
    LOWER_IMPLANT_IMPRESSION_3 = 63,

    UPPER_IMPLANT_IMPRESSION_1 = 71,
    UPPER_IMPLANT_IMPRESSION_2 = 72,
    UPPER_IMPLANT_IMPRESSION_3 = 73,

    LOWER_EDENTULOUS_IMPRESSION_1 = 81,
    LOWER_EDENTULOUS_IMPRESSION_2 = 82,
    LOWER_EDENTULOUS_IMPRESSION_3 = 83,

    UPPER_EDENTULOUS_IMPRESSION_1 = 91,
    UPPER_EDENTULOUS_IMPRESSION_2 = 92,
    UPPER_EDENTULOUS_IMPRESSION_3 = 93,
    #extra bite group 1
    BITE_7 = 100,
    BITE_8 = 101,
    BITE_9 = 102,
    BITE_10 = 103,
    BITE_11 = 104,
    BITE_12 = 105,
    #extra bite group 2
    BITE_13 = 106,
    BITE_14 = 107,
    BITE_15 = 108,
    BITE_16 = 109,
    BITE_17 = 110,
    BITE_18 = 111,
    #extra bite group 3
    BITE_19 = 112,
    BITE_20 = 113,
    BITE_21 = 114,
    BITE_22 = 115,
    BITE_23 = 116,
    BITE_24 = 117,
    #extra bite group 4
    BITE_25 = 118,
    BITE_26 = 119,
    BITE_27 = 120,
    BITE_28 = 121,
    BITE_29 = 122,
    BITE_30 = 123,

    LOWER_EMERGENCE_PROFILE = 130,
    UPPER_EMERGENCE_PROFILE = 131,

    LOWER_DENTURE = 140,
    UPPER_DENTURE = 141,

    EXTRA_JAW_1 = 200,
    EXTRA_JAW_2 = 201,
    EXTRA_JAW_3 = 202