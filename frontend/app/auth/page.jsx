'use client'

import { getCookie, setCookie } from 'cookies-next';
import { useRouter } from 'next/navigation'
import { useState } from 'react';

import Header from '../components/header'

export default function Login() {
    const router = useRouter()
    const token = getCookie('XToken') !== undefined ? getCookie('XToken') : null;
    const tokenExists = token !== (null && undefined)? true : false;

    const [loginValue, setLoginValue] = useState('');
    const [passwordValue, setPasswordValue] = useState('');

    let dataToSend = {}
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const urls = {
            loginUrl: 'http://localhost/api/login',
        }
        switch(tokenExists){
            case false:
                dataToSend = {
                    "password": passwordValue,
                    "login": loginValue,            
                };
                try {
                    let res = await fetch(urls.loginUrl, {
                      method: "POST",
                      body: JSON.stringify(dataToSend),
                      headers: {
                        'Content-Type': 'application/json',
                      }
                    });
                    let data = await res.json();
                    
                    if(data.access_token !== (undefined && null && "")) {
                       
                       setCookie('XToken', `${data.access_token}`, {'max-age': 2592000, 'path': '/'});
                       setCookie('userRoleId', `${data.role_id}`, {'max-age': 2592000, 'path': '/'});

                     
                      router.push('/lk/')
                    } else if(!data.success) {
                        alert('Неправильные логин и/или пароль!');
                        setLoginValue('')
                        setPasswordValue('')
                    }
                  } catch (err) {
                    alert(err);
                  }
                  break;
                case true:
                    router.push('/lk/')
                    break;
        }
       
                
    }

  
            return (
                <>
                    <Header isForLk={false}/>
                        <section>
                            <div className="container-xl">
                                <div className="b_h1 text-center">
                                    Войдите
                                </div>
                              <div className="d-flex flex-column align-items-center ">
                                 <div className="w-100 w-lg-50 ">
                                    <form onSubmit={handleSubmit} className="login_form" >
                                        <input 
                                        key={1}
                                        required
                                        className="b_input"
                                        placeholder="Логин"
                                        name="user_login"
                                        id="user_login"
                                        type="text"
                                        value={loginValue}
                                        onChange={(e) => setLoginValue(e.target.value)}
                                        ></input>
                                          <input 
                                          required
                                          key={2}
                                        className="b_input"
                                        placeholder="Пароль"
                                        name="user_password"
                                        id="user_password"
                                        value={passwordValue}
                                        type="password"
                                        onChange={(e) => setPasswordValue(e.target.value)}
                                        ></input>
                                        <button className="b_btn_main w-100"
                                        type="submit"
                                        > Войти</button>
                                    </form>
                                  
                                </div>
                              </div>
                            </div>
                        </section>
      
                </>
            )

}