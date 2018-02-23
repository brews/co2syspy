import pytest
import numpy as np
import co2sys


def test_CO2SYS():
    """Very basic smoke test for CO2SYS
    """

    # Conditions used in Mg/Ca forward model test case.
    par1type =    1 # The first parameter supplied is of type "1", which is "alkalinity"
    par2type =    2 # The first parameter supplied is of type "2", which is "DIC"
    par3type =    3 # The first parameter supplied is of type "3", which is "pH"
    presin   =    4.036785269144779e3 # Pressure    at input conditions
    tempout  =    0 # Temperature at output conditions - doesn't matter in this example
    presout  =    0 # Pressure    at output conditions - doesn't matter in this example
    pHscale  =    1 # pH scale at which the input pH is reported ("1" means "Total Scale")  - doesn't matter in this example
    k1k2c    =    4 # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    kso4c    =    1 # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
    alk_s = 2.337701660156250e3
    dic_s = 2.186364257812500e3
    sal_s = 34.875812530517578
    temp_s = 2.197510004043579
    si_s = 49.758834838867188
    p_s = 1.458118438720703

    out, niceheaders = co2sys.CO2SYS(alk_s, dic_s, par1type, par2type, sal_s, temp_s, tempout, presin, presout, si_s, p_s, pHscale, k1k2c, kso4c)

    # Testing against CO2SYS (MATLAB v1.1) - God save us all.
    np.testing.assert_allclose(out['TAlk'], 2.337701660156250e+03, atol=1e-8)
    np.testing.assert_allclose(out['TCO2'], 2.186364257812500e+03, atol=1e-8)
    np.testing.assert_allclose(out['pHin'], 7.926358670659251, atol=1e-8)
    np.testing.assert_allclose(out['pCO2in'], 3.339176636623637e+02, atol=1e-8)
    np.testing.assert_allclose(out['fCO2in'], 3.324931306109210e+02, atol=1e-8)
    np.testing.assert_allclose(out['HCO3in'], 2.063984353536685e+03, atol=1e-8)
    np.testing.assert_allclose(out['CO3in'], 1.031503927006473e+02, atol=1e-8)
    np.testing.assert_allclose(out['CO2in'], 19.229511575167592, atol=1e-8)
    np.testing.assert_allclose(out['BAlkin'], 64.136510368697373, atol=1e-8)
    np.testing.assert_allclose(out['OHin'], 0.740362148764086, atol=1e-8)
    np.testing.assert_allclose(out['PAlkin'], 1.524484881016718, atol=1e-8)
    np.testing.assert_allclose(out['SiAlkin'], 1.027218899018952, atol=1e-8)
    np.testing.assert_allclose(out['Hfreein'], 0.010960202071109, atol=1e-8)
    np.testing.assert_allclose(out['RFin'], 14.447365360053329, atol=1e-8)
    np.testing.assert_allclose(out['OmegaCAin'], 1.109015460859011, atol=1e-8)
    np.testing.assert_allclose(out['OmegaARin'], 0.733349633282838, atol=1e-8)
    np.testing.assert_allclose(out['xCO2in'], 3.362462277278146e+02, atol=1e-8)
    np.testing.assert_allclose(out['pHout'], 8.122966233696896, atol=1e-8)
    np.testing.assert_allclose(out['pCO2out'], 3.212196594903900e+02, atol=1e-8)
    np.testing.assert_allclose(out['fCO2out'], 3.198082412817060e+02, atol=1e-8)
    np.testing.assert_allclose(out['HCO3out'], 2.055541950520533e+03, atol=1e-8)
    np.testing.assert_allclose(out['CO3out'], 1.107009226494601e+02, atol=1e-8)
    np.testing.assert_allclose(out['CO2out'], 20.121384642507195, atol=1e-8)
    np.testing.assert_allclose(out['BAlkout'], 57.722997496438055, atol=1e-8)
    np.testing.assert_allclose(out['OHout'], 0.653911606741942, atol=1e-8)
    np.testing.assert_allclose(out['PAlkout'], 1.515025862046792, atol=1e-8)
    np.testing.assert_allclose(out['SiAlkout'], 0.873517831066995, atol=1e-8)
    np.testing.assert_allclose(out['Hfreeout'], 0.006859198847034, atol=1e-8)
    np.testing.assert_allclose(out['RFout'], 14.288317572981429, atol=1e-8)
    np.testing.assert_allclose(out['OmegaCAout'], 2.655081296144144, atol=1e-8)
    np.testing.assert_allclose(out['OmegaARout'], 1.668150040994507, atol=1e-8)
    np.testing.assert_allclose(out['xCO2out'], 3.231299189119258e+02, atol=1e-8)
    np.testing.assert_allclose(out['pHinTOTAL'], 7.926358670659251, atol=1e-8)
    np.testing.assert_allclose(out['pHinSWS'], 7.920051143153011, atol=1e-8)
    np.testing.assert_allclose(out['pHinFREE'], 7.960181438775133, atol=1e-8)
    np.testing.assert_allclose(out['pHinNBS'], 8.016658362436013, atol=1e-8)
    np.testing.assert_allclose(out['pHoutTOTAL'], 8.122966233696896, atol=1e-8)
    np.testing.assert_allclose(out['pHoutSWS'], 8.116021698995990, atol=1e-8)
    np.testing.assert_allclose(out['pHoutFREE'], 8.163726606834221, atol=1e-8)
    np.testing.assert_allclose(out['pHoutNBS'], 8.208086818347853, atol=1e-8)
    np.testing.assert_allclose(out['TEMPIN'], 2.197510004043579, atol=1e-8)
    np.testing.assert_allclose(out['TEMPOUT'], 0, atol=1e-8)
    np.testing.assert_allclose(out['PRESIN'], 4.036785269144779e+03, atol=1e-8)
    np.testing.assert_allclose(out['PRESOUT'], 0, atol=1e-8)
    assert out['PAR1TYPE'] == 1
    assert out['PAR2TYPE'] == 2
    np.testing.assert_allclose(out['PRESOUT'], 0, atol=1e-8)
    assert out['K1K2CONSTANTS'] == 4
    assert out['KSO4CONSTANTS'] == 1
    assert out['pHSCALEIN'] == 1
    np.testing.assert_allclose(out['SAL'], 34.875812530517578, atol=1e-8)
    np.testing.assert_allclose(out['PO4'], 1.458118438720703, atol=1e-8)
    np.testing.assert_allclose(out['SI'], 49.758834838867188, atol=1e-8)
