# -*- coding: utf-8 -*-
class Borg():
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind

    TO_SAE = "http://freesz.sinaapp.com/api/"
    # all kinds of security abt. set
    TOKEN =  "freesz"
    APPKEY = "wxf634634e44823957"
    SECRET = "de2d4bc65ec2ff4909dbc5e1d0e4b6f7"

    WX_GDG = 'gh_949ea152199b'
    AS_SRV = WX_GDG
    AS_USR = "oSslCs7WZ1aTsj4z-wZfUchXfsEc"

    # for douban
    WECHAT_API_KEY = '020a9c5869bcf26b061fd5093d36d741'
    WECHAT_API_SECRET = '2e6e4d4785a8c438'
    WECHAT_REDIRECT_URI = 'http://freesz.sinaapp.com/douban'
    WECHAT_SCOPE = 'douban_basic_common,book_basic_r,book_basic_w'

    LOGIN_API_KEY = '09009bd8ce37c64f1b01d38a6aa752ed'
    LOGIN_API_SECRET = 'd2cc229aa607ae60'
    LOGIN_REDIRECT_URI = 'http://freesz.sinaapp.com/login'
    LOGIN_SCOPE = 'douban_basic_common,book_basic_r,book_basic_w'

XCFG = Borg()

