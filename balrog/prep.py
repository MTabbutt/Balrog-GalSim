"""
code to download and prepare all the inputs we need as
input to balrog
"""

def prepare_tile(conf, tilename, band, clean=False):
    """
    download files needed for balrog, and make
    null weight files

    TODO: clean should remove more stuff, currently it only
    removes the null weight files, as done by the preparator
    """
    import desmeds

    prep=desmeds.desdm_maker.Preparator(
        conf,
        tilename,
        band,
    )

    if clean:
        prep.remove_nullwt()
    else:
        prep.go()

    return prep
