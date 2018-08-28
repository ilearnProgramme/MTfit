import unittest
import os
import sys
import tempfile
import glob
import shutil

import numpy as np

from MTfit.utilities.file_io import _convert_mt_space_to_struct
from MTfit.run import MTfit


class RunTestCase(unittest.TestCase):

    def setUp(self):
        self.cwd = os.getcwd()
        if sys.version_info >= (3, 0):
            self.tempdir = tempfile.TemporaryDirectory()
            os.chdir(self.tempdir.name)
        else:
            self.tempdir = tempfile.mkdtemp()
            os.chdir(self.tempdir)

    def tearDown(self):
        os.chdir(self.cwd)
        if sys.version_info >= (3, 0):
            self.tempdir.cleanup()
        else:
            try:
                shutil.rmtree(self.tempdir)
            except:
                pass

    def test_MTfit(self):
        logfiles = glob.glob('*.log')
        import numpy as np
        data = {'PPolarity': {'Stations': {'Name': ['S0649', "S0162", "S0083"], 'Azimuth': np.array([90.0, 270.0, 180.0]), 'TakeOffAngle': np.array([30.0, 60.0, 35.])},
                              'Measured': np.matrix([[1], [-1], [-1]]), 'Error': np.matrix([[0.001], [0.5], [0.02]])}}
        MTfit(data, max_time=10, phy_mem=0.5, parallel=False, convert=False)
        self.assertTrue(os.path.exists('MTfitOutputMT.mat'))
        os.remove('MTfitOutputMT.mat')
        newlogfiles = glob.glob('*.log')
        for logfile in newlogfiles:
            if logfile not in logfiles:
                os.remove(logfile)

    def test_combine_mpi_output(self):
        self.output_mpi()
        MTfit(datafile='./', combine_mpi_output=True, max_time=10,
              phy_mem=0.5, parallel=False, convert=True, binary_file_version=2)
        self.assertTrue(os.path.exists('20120620223428431DC.mat'))
        self.clean_mpi()

    def output_mpi(self):
        uid = "20120620223428431"
        inv_file = "(dp0\nS'PPolarity'\np1\n(dp2\nS'Error'\np3\ncnumpy.core.multiarray\n_reconstruct\np4\n(cnumpy.matrixlib.defmatrix\nmatrix\np5\n(I0\ntp6\nS'b'\np7\ntp8\nRp9\n(I1\n(I19\nI1\ntp10\ncnumpy\ndtype\np11\n(S'f8'\np12\nI0\nI1\ntp13\nRp14\n(I3\nS'<'\np15\nNNNI-1\nI-1\nI0\ntp16\nbI01\nS'\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?{\\x14\\xaeG\\xe1z\\x84?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?\\xfc\\xa9\\xf1\\xd2MbP?'\np17\ntp18\nbsS'Measured'\np19\ng4\n(g5\n(I0\ntp20\ng7\ntp21\nRp22\n(I1\n(I19\nI1\ntp23\ng11\n(S'i8'\np24\nI0\nI1\ntp25\nRp26\n(I3\nS'<'\np27\nNNNI-1\nI-1\nI0\ntp28\nbI01\nS'\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff'\np29\ntp30\nbsS'Stations'\np31\n(dp32\nS'TakeOffAngle'\np33\ng4\n(g5\n(I0\ntp34\ng7\ntp35\nRp36\n(I1\n(I19\nI1\ntp37\ng14\nI01\nS'\\x00\\x00\\x00\\x00\\x00@W@fffff6a@ffffffP@\\x9a\\x99\\x99\\x99\\x99\\xf9V@\\x9a\\x99\\x99\\x99\\x99YP@\\xcd\\xcc\\xcc\\xcc\\xcc\\xacQ@fffffFP@\\x00\\x00\\x00\\x00\\x00@P@fffff&Q@\\x9a\\x99\\x99\\x99\\x999Q@\\x00\\x00\\x00\\x00\\x00\\xa0V@\\xcd\\xcc\\xcc\\xcc\\xccLP@33333\\xf3K@\\xcd\\xcc\\xcc\\xcc\\xccL[@\\x00\\x00\\x00\\x00\\x00@L@33333\\xb3W@fffff\\xc6T@\\xcd\\xcc\\xcc\\xcc\\xccLP@33333\\xf3W@'\np38\ntp39\nbsS'Name'\np40\n(lp41\nS'BURF'\np42\naS'REN'\np43\naS'GHA'\np44\naS'K190'\np45\naS'SKI'\np46\naS'BLAF'\np47\naS'N66D'\np48\naS'VVAT'\np49\naS'K008'\np50\naS'SKOG'\np51\naS'HVAN'\np52\naS'GUDF'\np53\naS'SVA'\np54\naS'K250'\np55\naS'BUNG'\np56\naS'KVO'\np57\naS'TREB'\np58\naS'KODA'\np59\naS'K115'\np60\nasS'Azimuth'\np61\ng4\n(g5\n(I0\ntp62\ng7\ntp63\nRp64\n(I1\n(I19\nI1\ntp65\ng14\nI01\nS'\\xcd\\xcc\\xcc\\xcc\\xcc\\xac\\\\@fffff\\xe6r@\\x00\\x00\\x00\\x00\\x00\\x005@fffff~s@\\x9a\\x99\\x99\\x99\\x99qu@\\x9a\\x99\\x99\\x99\\x99\\te@fffffVv@\\x9a\\x99\\x99\\x99\\x99yv@\\x9a\\x99\\x99\\x99\\x99\\x99%@fffff\\xc6[@fffff\\xf6c@33333\\xe3u@\\xcd\\xcc\\xcc\\xcc\\xcc\\xfci@ffffffL@\\x00\\x00\\x00\\x00\\x00\\x00!@fffff\\xfeu@\\x9a\\x99\\x99\\x99\\x999e@33333#f@33333;v@'\np66\ntp67\nbsssS'UID'\np68\nS'20120620223428431'\np69\ns."
        # We'll use _convert_mt_to_struct code to generate the inputs
        mt_0, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[1, 0, 0, 1],
                                                                                                           [0, 1, 1, 0],
                                                                                                           [0, 0, 0, 0],
                                                                                                           [0, 0, 0, 0],
                                                                                                           [0, 0, 0, 0],
                                                                                                           [0, 0, 0, 0]]),
                                               'probability': np.array([0.2, 0.3, 0.4, 0.5]),
                                               'ln_pdf': np.log(np.array([0.2, 0.3, 0.4, 0.5]))})
        mt_11, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[1, 0, 0, 1],
                                                                                                            [0, 1, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 1, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0]]),
                                                'probability': np.array([0.2, 0.3, 0.4, 0.5]),
                                                'ln_pdf': np.log(np.array([0.2, 0.3, 0.4, 0.5]))})
        mt_2, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[1, 0, 0, 1],
                                                                                                            [0, 1, 1, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0.5, 0, 0, 0],
                                                                                                            [0, 0, 0, 0]]),
                                               'probability': np.array([0.2, 0.3, 0.4, 0.5]),
                                               'ln_pdf': np.log(np.array([0.2, 0.3, 0.4, 0.5]))})
        mt_4, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[1, 0, 0, 1],
                                                                                                            [0, 1, 2, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [1, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0]]),
                                               'probability': np.array([0.2, 0.3, 0.4, 0.5]),
                                               'ln_pdf': np.log(np.array([0.2, 0.3, 0.4, 0.5]))})
        mt_5, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[1, 0, 0, 0.5],
                                                                                                            [0, 0, 1, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 1, 0, 0.5],
                                                                                                            [0, 0, 0, 0]]),
                                               'probability': np.array([0.2, 0.3, 0.4, 0.5]),
                                               'ln_pdf': np.log(np.array([0.2, 0.3, 0.4, 0.5]))})
        mt_7, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[0, 0, 0, 1],
                                                                                                            [0, 0, 1, 0],
                                                                                                            [1, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 1, 0, 0]]),
                                               'probability': np.array([0.1, 0.8, 0.05, 0.1]),
                                               'ln_pdf': np.log(np.array([0.1, 0.8, 0.05, 0.1]))})
        mt_9, _ = _convert_mt_space_to_struct({'total_number_samples': 28, 'moment_tensor_space': np.array([[0, 0, 0, 1],
                                                                                                            [0, 0, 1, 0],
                                                                                                            [1, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 0, 0, 0],
                                                                                                            [0, 1, 0, 0]]),
                                               'probability': np.array([0.1, 0.8, 0.05, 0.1]),
                                               'ln_pdf': np.log(np.array([0.1, 0.8, 0.05, 0.1]))})
        mts = [mt_0, mt_2, mt_4, mt_5, mt_7, mt_9, mt_11]
        hyp_0 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.417409\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 181.514368855 57.4273143295 -63.7772524032 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_11 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.415002\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 177.556091042 49.9167309676 -60.0047005874 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_2 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.418674\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 173.928528225 49.2251020408 -62.1497735771 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_4 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.402503\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 176.306084139 49.4840610926 -61.7393950117 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_5 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.400688\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 174.466781333 51.9113260108 -62.8997997587 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_7 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.380454\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 172.998180007 53.0423359237 -65.3105632286 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyp_9 = 'NLLOC 20120620223428431\nSIGNATURE MTfit 1.0.0B/2015-10-21T16:42:43.389123\nCOMMENT MTfit inversion\nGRID None\nSEARCH None\nHYPOCENTER x ? y ? z ? OT ? ix ? iy ? iz ?\nGEOGRAPHIC OT ? ? ? ? ? ? Lat ? Long ? Depth ?\nQUALITY Pmax ? MFmin ? MFmax ? RMS ? Nphs ? Gap ? Dist ? Mamp ? ? Mdur ? ?\nVPVSRATIO ? ?\nSTATISTICS ExpectX ? Y ? Z ? CovXX ? XY ? XZ ? YY ? YZ ? ZZ ? EllAz1 ? Dip1 ? Len1 ? Az2 ? Dip2 ? Len2 ? Len3 ?\nTRANS None\nFOCALMECH ? ? ? Mech 174.543220852 47.6657193922 -64.744243488 mf 0 nObs 0\nPHASE ID Ins Cmp On Pha FM Date HrMn Sec Err ErrMag Coda Amp Per > TTpred Res Weight StaLoc(X Y Z) SDist SAzim RAz RDip RQual Tcorr\nBURF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 114.7 93.0 ? ?\nREN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 302.4 137.7 ? ?\nGHA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 21.0 65.6 ? ?\nK190 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 311.9 91.9 ? ?\nSKI ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 343.1 65.4 ? ?\nBLAF ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 168.3 70.7 ? ?\nN66D ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 357.4 65.1 ? ?\nVVAT ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 359.6 65.0 ? ?\nK008 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 10.8 68.6 ? ?\nSKOG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 111.1 68.9 ? ?\nHVAN ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 159.7 90.5 ? ?\nGUDF ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 350.2 65.2 ? ?\nSVA ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 207.9 55.9 ? ?\nK250 ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 56.8 109.2 ? ?\nBUNG ? ? ? P U ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 8.5 56.5 ? ?\nKVO ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 351.9 94.8 ? ?\nTREB ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 169.8 83.1 ? ?\nKODA ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 177.1 65.2 ? ?\nK115 ? ? ? P D ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? 355.7 95.8 ? ?\nEND_PHASE\nEND_NLLOC\n'
        hyps = [hyp_0, hyp_2, hyp_4, hyp_5, hyp_7, hyp_9, hyp_11]
        out = [0, 2, 4, 5, 7, 9, 11]
        open(uid+'.inv', 'w').write(inv_file)
        for j, i in enumerate(out):
            open(uid+'DC.'+str(i)+'.mt', 'wb').write(mts[j])
            open(uid+'DC.'+str(i)+'.hyp', 'w').write(hyps[j])

    def clean_mpi(self):
        uid = "20120620223428431"
        try:
            os.remove(uid+'.inv')
        except Exception:
            pass
        try:
            os.remove(uid+'DC.0.pkl')
        except Exception:
            pass
        out = [0, 2, 4, 5, 7, 9, 11]
        for i in out:
            try:
                os.remove(uid+'DC.'+str(i)+'.mt')
            except Exception:
                pass
            try:
                os.remove(uid+'DC.'+str(i)+'.hyp')
            except Exception:
                pass
        try:
            os.remove(uid+'DC.mat')
        except Exception:
            pass
