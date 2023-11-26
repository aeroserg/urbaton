'use client'

import { useRouter } from 'next/navigation';
import { useState,useEffect } from 'react';
import Header from '../components/header';

export default function Order() {
    const [schoolsData, setSchoolsData] = useState({
        schools: []
    })

    useEffect(() => {
        const HOST = location.protocol + '//' + location.host

        fetch(`${HOST}/api/all_schools`, {
            method: "GET"
        })
        .then(response => response.json())
        .then(data => {
            setSchoolsData(data)
            setSchoolId(data.schools[0].id)
            }
        ) 
    },[])

    const router = useRouter()
    const [emailValue, setEmailValue] = useState('');
    const [nameValue, setNameValue] = useState('');
    const [surnameValue, setSurnameValue] = useState('');
    const [phoneValue, setPhoneValue] = useState('');
    
    const [childEmailValue, setChildEmailValue] = useState('');
    const [childNameValue, setChildNameValue] = useState('');
    const [childSurnameValue, setChildSurnameValue] = useState('');
    const [childPhoneValue, setChildPhoneValue] = useState('');

    const [selectValue, setSelectedValue] = useState('Выберете учебное заведение')
    const [schoolId, setSchoolId] = useState(0)

    let dataToSend = {}
    console.log(schoolId)
    const handleSubmit = async (e) => {
        e.preventDefault();
        let elements = e.target.elements;
        for (var i = 0, len = elements.length; i < len; ++i) {
            elements[i].readOnly = true;
            console.log(123)
        }
        const HOST = location.protocol + '//' + location.host

        const urls = {
            order: `${HOST}/api/new_order`,
        }
        dataToSend = {
            parent: 
                {
                    first_name: nameValue,
                    last_name: surnameValue,
                    email: emailValue,
                    phone_number: phoneValue,
                    school_id:schoolId
                },
            student: 
                {
                    first_name: childNameValue,
                    last_name: childSurnameValue,
                    email: childEmailValue,
                    phone_number: childPhoneValue,
                    school_id:schoolId
                }     
        };
        console.log(dataToSend)
        try {
            let res = await fetch(urls.order, {
                method: "POST",
                body: JSON.stringify(dataToSend),
                headers: {
                'Content-Type': 'application/json',
                }
            });
            let data = await res.json();
            console.log(data)
            if(data.user_created) {
                alert('Заявка отправлена успешно!')
                for (var i = 0, len = elements.length; i < len; ++i) {
                    elements[i].readOnly = false;
                }
                router.refresh()
            } else {
                alert('Что-то пошло не так');
                for (var i = 0, len = elements.length; i < len; ++i) {
                    elements[i].readOnly = false;
                }
                router.refresh()
            }
            } catch (err) {
            alert(err);
            }                
    }
    return(
        <>
        <Header />
            <div className="container-lg">
                <div className="order_inner d-flex align-items-center my-5 row">
                <div className="order_text col-lg-4 col-12">
                    <h1>Расскажем про занятия <strong>и запишем в группу</strong></h1>
                </div>
                <div className="col-lg-6 offset-lg-2 col-12">
                    <h3 className="text-center">Заполните данные ниже, 
и мы ответим вам сегодня</h3>
                                    <form onSubmit={handleSubmit} className="login_form" >
                                        <input 
                                        key={1}
                                        required
                                        className="b_input"
                                        placeholder="Имя"
                                        name="user_name"
                                        id="user_name"
                                        type="text"
                                        value={nameValue}
                                        onChange={(e) => setNameValue(e.target.value)}
                                        ></input>
                                          <input 
                                        key={2}
                                        required
                                        className="b_input"
                                        placeholder="Фамилия"
                                        name="user_surname"
                                        id="user_surname"
                                        type="text"
                                        value={surnameValue}
                                        onChange={(e) => setSurnameValue(e.target.value)}
                                        ></input>
                                          <input 
                                          required
                                          key={3}
                                        className="b_input"
                                        placeholder="Телефон"
                                        name="user_phone"
                                        id="user_phone"
                                        value={phoneValue}
                                        type="text"
                                        onChange={(e) => setPhoneValue(e.target.value)}
                                        ></input>
                                         <input 
                                          required
                                          key={4}
                                        className="b_input"
                                        placeholder="Email"
                                        name="user_email"
                                        id="user_email"
                                        value={emailValue}
                                        type="text"
                                        onChange={(e) => setEmailValue(e.target.value)}
                                        ></input>


                                         <input 
                                        key={5}
                                        required
                                        className="b_input"
                                        placeholder="Имя ребенка"
                                        name="user_child_name"
                                        id="user_child_name"
                                        type="text"
                                        value={childNameValue}
                                        onChange={(e) => setChildNameValue(e.target.value)}
                                        ></input>
                                          <input 
                                        key={6}
                                        required
                                        className="b_input"
                                        placeholder="Фамилия ребенка"
                                        name="user_child_surname"
                                        id="user_child_surname"
                                        type="text"
                                        value={childSurnameValue}
                                        onChange={(e) => setChildSurnameValue(e.target.value)}
                                        ></input>
                                          <input 
                                          required
                                          key={7}
                                        className="b_input"
                                        placeholder="Телефон"
                                        name="user_child_phone"
                                        id="user_child_phone"
                                        value={childPhoneValue}
                                        type="text"
                                        onChange={(e) => setChildPhoneValue(e.target.value)}
                                        ></input>
                                         <input 
                                          required
                                          key={8}
                                        className="b_input"
                                        placeholder="Email ребенка (логин)"
                                        name="user_child_email"
                                        id="user_child_email"
                                        value={childEmailValue}
                                        type="text"
                                        onChange={(e) => setChildEmailValue(e.target.value)}
                                        ></input>
                                        <select id={schoolId} value={selectValue} onChange={(e) => {setSelectedValue(e.target.value); setSchoolId(e.target.selectedOptions[0].attributes.id.value)}} name="select_school">
                                            {schoolsData.schools ? schoolsData.schools.map((item) => (
                                                <option id={item.id} value={item.name} key={item.id}>{item.name}</option>
                                            )) : undefined}
                                        </select>
                                        <button className="b_btn_main w-100"
                                        type="submit"
                                        > Войти</button>
                                    </form>
                                  
                                </div>
                </div>
            </div>
        </>
    )
}