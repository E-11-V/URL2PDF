
import tempfile
import urllib.request
import fpdf
import socket

def jpgs_to_pdf(jpg_urls, pdf_filename):
    pdf = fpdf.FPDF(format='letter')

    for url in jpg_urls:
        try:
            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
                # set timeout for the request
                socket.setdefaulttimeout(10) 
                f.write(urllib.request.urlopen(url).read())
                pdf.add_page()
                pdf.image(f.name, x=0, y=0, w=210, h=297)
        except Exception as e:
            print(f'Error processing {url}: {e}')

    pdf.output(pdf_filename, 'F')



    
jpg_urls = [
    "https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0001_al_piatto.anteriore.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0002_ba_risguardia.anteriore.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0003_cy_0001r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0004_cy_0001v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0005_fa_0001r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0006_fa_0001v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0007_fa_0002r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0008_fa_0002v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0009_fa_0003r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0010_fa_0003v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0011_fa_0004r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0012_fa_0004v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0013_fa_0005r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0014_fa_0005v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0015_fa_0006r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0016_fa_0006v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0017_fa_0007r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0018_fa_0007v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0019_fa_0008r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0020_fa_0008v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0021_fa_0009r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0022_fa_0009v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0023_fa_0010r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0024_fa_0010v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0025_fa_0011r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0026_fa_0011v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0027_fa_0012r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0028_fa_0012v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0029_fa_0013r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0030_fa_0013v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0031_fa_0014r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0032_fa_0014v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0033_fa_0015r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0034_fa_0015v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0035_fa_0016r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0036_fa_0016v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0037_fa_0017r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0038_fa_0017v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0039_fa_0018r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0040_fa_0018v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0041_fa_0019r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0042_fa_0019v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0043_fa_0020r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0044_fa_0020v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0045_fa_0021r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0046_fa_0021v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0047_fa_0022r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0048_fa_0022v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0049_fa_0023r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0050_fa_0023v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0051_fa_0024r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0052_fa_0024v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0053_fa_0025r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0054_fa_0025v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0055_fa_0026r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0056_fa_0026v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0057_fa_0027r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0058_fa_0027v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0059_fa_0028r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0060_fa_0028v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0061_fa_0029r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0062_fa_0029v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0063_fa_0030r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0064_fa_0030v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0065_fa_0031r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0066_fa_0031v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0067_fa_0032r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0068_fa_0032v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0069_fa_0033r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0070_fa_0033v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0071_fa_0034r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0072_fa_0034v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0073_fa_0035r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0074_fa_0035v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0075_fa_0036r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0076_fa_0036v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0077_fa_0037r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0078_fa_0037v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0079_fa_0038r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0080_fa_0038v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0081_fa_0039r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0082_fa_0039v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0083_fa_0040r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0084_fa_0040v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0085_fa_0041r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0086_fa_0041v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0087_fa_0042r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0088_fa_0042v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0089_fa_0043r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0090_fa_0043v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0091_fa_0044r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0092_fa_0044v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0093_fa_0045r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0094_fa_0045v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0095_fa_0046r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0096_fa_0046v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0097_fa_0047r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0098_fa_0047v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0099_fa_0048r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0100_fa_0048v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0101_fa_0049r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0102_fa_0049v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0103_fa_0050r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0104_fa_0050v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0105_fa_0051r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0106_fa_0051v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0107_fa_0052r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0108_fa_0052v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0109_fa_0053r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0110_fa_0053v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0111_fa_0054r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0112_fa_0054v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0113_fa_0055r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0114_fa_0055v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0115_fa_0056r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0116_fa_0056v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0117_fa_0057r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0118_fa_0057v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0119_fa_0058r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0120_fa_0058v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0121_fa_0059r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0122_fa_0059v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0123_fa_0060r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0124_fa_0060v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0125_fa_0061r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0126_fa_0061v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0127_fa_0062r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0128_fa_0062v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0129_fa_0063r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0130_fa_0063v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0131_fa_0064r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0132_fa_0064v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0133_fa_0065r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0134_fa_0065v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0135_fa_0066r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0136_fa_0066v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0137_fa_0067r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0138_fa_0067v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0139_fa_0068r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0140_fa_0068v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0141_fa_0069r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0142_fa_0069v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0143_fa_0070r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0144_fa_0070v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0145_fa_0071r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0146_fa_0071v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0147_fa_0072r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0148_fa_0072v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0149_fa_0073r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0150_fa_0073v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0151_fa_0074r.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0152_fa_0074v.jp2/full/2132,/0/native.jpg",
"https://digi.vatlib.it/pub/digit/MSS_Vat.lat.5581/iiif/Vat.lat.5581_0153_fa_0075r.jp2/full/2132,/0/native.jpg"

]

pdf_filename = "images.pdf"
jpgs_to_pdf(jpg_urls, pdf_filename)