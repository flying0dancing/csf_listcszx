from enum import Enum
class AcronymCatalogs(object):
    acqDict = {'3': 'Ipl', '4': 'Ipl', '130': 'Ipl', '131': 'Ipl',
               '6': 'Prp', '7': 'Prp',
               '8': 'Dnt', '9': 'Dnt', '140': 'Dnt', '141': 'Dnt',
               '200': 'Ext', '201': 'Ext', '202': 'Ext',
               '21': 'Ipr', '22': 'Ipr', '23': 'Ipr', '31': 'Ipr', '32': 'Ipr', '33': 'Ipr',
               '41': 'PrpIpr', '42': 'PrpIpr', '43': 'PrpIpr', '51': 'PrpIpr', '52': 'PrpIpr', '53': 'PrpIpr',
               '61': 'IplIpr', '62': 'IplIpr', '63': 'IplIpr', '71': 'IplIpr', '72': 'IplIpr', '73': 'IplIpr',
               '81': 'DntIpr', '82': 'DntIpr', '83': 'DntIpr', '91': 'DntIpr', '92': 'DntIpr', '93': 'DntIpr'}
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