#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request
import logging
import traceback
app = Flask(__name__)

#logger = logging.getLogger('app.module')
logging.basicConfig(level=logging.INFO,
                    filename='byb.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


@app.route('/byb/check', methods=["POST"])
def hello_world():
    mac = "unknown"
    try:
        num = request.form['num']
        info = request.form['info']
        mac = request.form['mac']
        logging.info('comming! mac: %s' %mac)

        if num == info == "AUTO":
            return 'HELLO'
        else:
            return 'ERROR'
    except Exception as e:    
        logging.info('comming! mac: %s' %mac)
        logging.error(str(e))
        s = traceback.format_exc()
        logging.error(s)
        return 'ERROR'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18081, debug=False)
