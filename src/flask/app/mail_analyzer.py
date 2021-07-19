#!/usr/bin/env python3
import email
import os
import mimetypes
import fsops
from werkzeug.utils import secure_filename
from argparse import ArgumentParser
import selenium_handler

# Set general assumptions on variables
selenium = False

def parsemail(file, directory):
    """
    parses an eml file and extracts its content
    :param file: path to eml file
    :return:
    """

    with open(file, 'rb') as fp:
        msg = email.message_from_binary_file(fp=fp, policy=email.policy.default)
    fsops.mkdir(directory)

    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        filename = secure_filename(part.get_filename())
        with open(os.path.join(directory, filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))


def get_body_links(file):
    """
    extracts urls from Email body
    :param file: email file
    :return: list of urls
    """
    links = []
    import re
    urlfinder = re.compile(r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""")
    with open(file, 'rb') as fp:
        msg = email.message_from_binary_file(fp=fp, policy=email.policy.default)
    body = msg.get_body(preferencelist=('related', 'html', 'plain'))
    links = re.findall(urlfinder, body)
    return links


def analyze(file, directory, selenium):
    """
    runs the full analysis suite on the email file
    :param file: Path to file
    :param directory: working directory
    :param selenium: if True, try to get screenshots of URLs
    :return:
    """
    working_dir = fsops.parentPath(file)
    contentdir = working_dir + 'message_contents'
    imagedir = working_dir + 'screenshots'
    filetype = mimetypes.guess_type(file)
    if filetype != 'message/rfc822':
        return "not a valid eml file"
    parsemail(file=file, directory=contentdir)
    fsops.mkdir(imagedir)
    if selenium == True:
        for link in get_body_links(file):
            selenium_handler.getScreenshot(url=link, imagedir=imagedir)




if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('emlfile')
    parser.add_argument('workdir')
    parser.add_argument('')
    args = parser.parse_args()
    analyze(args.emlfile)
