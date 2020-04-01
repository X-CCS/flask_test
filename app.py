from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import Length, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='secret string'


class Login(FlaskForm):
    username = StringField('用户名', validators=[Length(min=6, max=12, message='用户名(6-12)位'),
                                              DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[Length(min=6, max=12, message='密码(6-12)位'),
                                               DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')


@app.route('/wtfform/', methods=['GET', 'POST'])
def wtf_form():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form.get('username'))
            print(request.form.get('password'))
            return '登录成功'

    return render_template('wtf_form.html', form=form)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
