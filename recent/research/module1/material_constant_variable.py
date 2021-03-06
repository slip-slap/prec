"""
Maitain constant variable will be used in this program
"""

#FAILURE_CRITERIA = "max_stress"
FAILURE_CRITERIA = "tsai_wu"

GLASS_EPOXY= 'glass_epoxy'
GRAPHITE_EPOXY = "graphite_epoxy"
CARBON_EPOXY = "carbon_epoxy"
T300_5308 = "T300_5308"
GLASS_EPOXY_PROPERTIES     = {"E1":38.6,  "E2":8.27, "v12":0.26,  "G12":4.14 }
CARBON_EPOXY_PROPERTIES    = {"E1":116.6,  "E2":7.673, "v12":0.27,  "G12":4.173 }
GRAPHITE_EPOXY_PROPERTIES  = {"E1":181,  "E2":10.3, "v12":0.28,  "G12":7.17 }
T300_5308_PROPERTIES = {"E1":40.91,  "E2":9.88, "v12":0.292,  "G12":2.84 }


CARBON_EPOXY_DENSITY = 1.605*1000
GRAPHITE_EPOXY_DENSITY = 1.59*1000
GLASS_EPOXY_DENSITY = 1.97*1000

GLASS_EPOXY_COST = 1
GRAPHITE_EPOXY_COST = 2.5
CARBON_EPOXY_COST = 8



