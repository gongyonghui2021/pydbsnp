#===============================================================================
# env.py
#===============================================================================

"""Handling environment variables for pydbsnp"""




# Imports ======================================================================

import os
import os.path




# Constants ====================================================================

FTP_BASENAME_GRCH37 = 'GCF_000001405.25.bgz'
FTP_BASENAME_GRCH38 = 'GCF_000001405.38.bgz'
VCF_GRCH37 = os.environ.get(
    'PYDBSNP_VCF_GRCH37', 
    os.path.join(os.path.dirname(__file__), FTP_BASENAME_GRCH37)
)
VCF_GRCH38 = os.environ.get(
    'PYDBSNP_VCF_GRCH38', 
    os.path.join(os.path.dirname(__file__), FTP_BASENAME_GRCH38)
)
BUILD_TO_VCF = {
    'hg19': VCF_GRCH37, 'GRCh37': VCF_GRCH37,
    'hg38': VCF_GRCH38, 'GRCh38': VCF_GRCH38
}
BED_GRCH37 = os.environ.get(
    'PYDBSNP_BED_GRCH37', 
    os.path.join(os.path.dirname(__file__), 'GCF_000001405.25.bed.bgz')
)
BED_GRCH38 = os.environ.get(
    'PYDBSNP_BED_GRCH38', 
    os.path.join(os.path.dirname(__file__), 'GCF_000001405.38.bed.bgz')
)
