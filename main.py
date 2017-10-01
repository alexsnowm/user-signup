from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def splash():
    return render_template('splash.html')

@app.route('/signup', methods=['POST'])
def validate():
    username_err_msg = ''
    pass_err_msg = ''
    pass_conf_err_msg = ''
    eml_err_msg = ''

    username_mn_raw = request.form['username_field_ind_html']
    username_mn = cgi.escape(username_mn_raw, quote=True)

    pass_mn_raw = request.form['password_1st_field_ind_html']
    pass_mn = cgi.escape(pass_mn_raw, quote=True)

    pass_conf_mn_raw = request.form['password_conf_field_ind_html']
    pass_conf_mn = cgi.escape(pass_conf_mn_raw, quote=True)

    eml_mn_raw = request.form['eml_field_ind_html']
    eml_mn = cgi.escape(eml_mn_raw, quote=True)

    if (not username_mn) or (' ' in username_mn) or (len(username_mn) < 3) or (len(username_mn) > 20):
        username_err_msg = '''That's not a valid username'''

    if (not pass_mn) or (' ' in pass_mn) or (len(pass_mn) < 3) or (len(pass_mn) > 20):
        pass_err_msg = '''That's not a valid password'''

    if pass_conf_mn != pass_mn:
        pass_conf_err_msg = '''Passwords don't match'''

    if eml_mn and ((eml_mn.count('@') != 1) or (eml_mn.count('.') != 1) or (' ' in eml_mn) or (len(eml_mn) < 3) or (len(eml_mn) > 20)):
        eml_err_msg = '''That's not a valid email'''

    if not username_err_msg and not pass_err_msg and not pass_conf_err_msg and not eml_err_msg:
        return redirect('/welcome?username={0}'.format(username_mn))
    else:
        return render_template('splash.html', entd_username=username_mn,username_err=username_err_msg,password_1st_err=pass_err_msg,password_conf_err=pass_conf_err_msg,entd_eml=eml_mn,eml_err=eml_err_msg)


@app.route('/welcome', methods=['GET'])
def welcome_pg():
    username_wel_mn = request.args.get('username')

    return render_template('welcome.html',username_wel_html=username_wel_mn)

app.run()