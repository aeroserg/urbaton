'use client'

import Header from "./header"
import { useEffect, useState } from "react"
import { getCookie } from "cookies-next"

export default function LkForAdmin(){
    const [daysArray,setDayArray] = useState([])
    const [isPressed, setIsPressed] = useState(false)
    
    const [parallelValue, setParallelValue] = useState('')
    const [classValue, setClassValue] = useState('')

    const [timeValue, setTimeValue] = useState(`${new Date().getFullYear()}-${new Date().getMonth()+1}`)
    const [pupilValue, setPupilValue] = useState('')

    const [parId,setParId] = useState(0)
    const [classId,setClassId] = useState(0)
    const [pupilIdValue, setPupilIdValue] = useState(0)


    function getDaysQuantity(month, year) {
        return new Date(year, month, 0).getDate();
    } 
    const handleSubmit = async (e) => {
        e.preventDefault();
        let elements = e.target.elements;
        for (var i = 0, len = elements.length; i < len; ++i) {
            elements[i].readOnly = true;
        }
        const urls = {
            order: 'http://localhost/api/',
        }
        dataToSend = {
          parallel: parId,
          class: classId,
          time: timeValue
        };
   
        try {
            let res = await fetch(urls.order, {
                method: "POST",
                body: JSON.stringify(dataToSend),
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${getCookie('XToken')}`
                }
            });
            let data = await res.json();
            console.log(data)
            if(data.success) {
                alert('Успешно добавлено')
                for (var i = 0, len = elements.length; i < len; ++i) {
                    elements[i].readOnly = false;
                }
               
            } else {
                alert('Что-то пошло не так');
                for (var i = 0, len = elements.length; i < len; ++i) {
                    elements[i].readOnly = false;
                }
                
            }
            } catch (err) {
            alert(err);
            }                
    }
    function handleClickIndividual() {
        setIsPressed(!isPressed)
    }
    const timeRanges = [
        {
            start: '13:00',
            finish: '13:45'
        },
        {
            start: '13:45',
            finish: '14:30'
        },
        {
            start: '14:30',
            finish: '15:15'
        },
        {
            start: '15:15',
            finish: '16:00'
        },
        {
            start: '16:00',
            finish: '16:45'
        },
        {
            start: '16:45',
            finish: '17:30'
        },
        {
            start: '17:30',
            finish: '18:15'
        },
        {
            start: '18:15',
            finish: '19:00'
        },
        {
            start: '19:00',
            finish: '19:45'
        },
        {
            start: '19:45',
            finish: '20:30'
        }
    ]
    const [isOpen, setIsOpen] = useState(false)
    function closeModal() {
        setIsOpen(false)
    }

    function openModal(id) {
        setIsOpen(!isOpen)
    }
    function changeForm() {
        daysArray.length = 0
        for(let j = 1; j <= getDaysQuantity(new Date(timeValue).getMonth()+1, new Date(timeValue).getFullYear()); j++) {
            daysArray[j-1] = (`${new Date(timeValue).getFullYear()}-${new Date(timeValue).getMonth()+1}-${j}`)
        }
        setTimeValue(daysArray);
        console.log(daysArray)
    }
    function Modal({...props}) {
        return (
            <>
                <div className="fillInTimeTable">

                </div>
            </>
        )
    }
    return(
        <>
            <Header isForLk={'school'} />
            <section className="l-section" onClick={closeModal}>
                <div className="container-md">
                    <div className="timetable">
                        <div className="b_title">Расписание</div>
                        <div className="form"> 
                        <select id={parId} value={parallelValue} onChange={(e) => {setParallelValue(e.target.value); setParId(e.target.selectedOptions[0].attributes.id.value); }} name="select_parallel">
                            <option id={11} value="1">Параллель 1</option>
                            <option id={21} value="2">Параллель 2</option>
                            <option id={31} value="3">Параллель 3</option>
                            <option id={41} value="4">Параллель 4</option>
                        </select>
                        <select id={classId} value={classValue} onChange={(event) => {setClassValue(event.target.value); setClassId(event.target.selectedOptions[0].attributes.id.value)}} name="select_class">
                            <option id={12} value="а">А</option>
                            <option id={22} value="б">Б</option>
                            <option id={32} value="в">В</option>
                            <option id={42} value="г">Г</option>
                        </select>
                        <input onChange={(e) => {setTimeValue(e.target.value)} }type="month" id="start" name="start" min="2023-08" value={timeValue}></input>
                        <div className="formRow mt-3">
                            <div className="b_checkbox_btn " data-state={isPressed} onClick={handleClickIndividual}>Индивидуальное расписание</div>
                            <select className="mt-0"  id={pupilIdValue} value={pupilValue} onChange={(e) => {setPupilValue(e.target.value); setPupilIdValue(e.target.selectedOptions[0].attributes.id.value)}} name="select_pupil">
                                <option id={13} value="Маша">Маша</option>
                                <option id={23} value="Петя">Петя</option>
                                <option id={33} value="Вася">Вася</option>
                                <option id={43} value="Гриша">Гриша</option>
                            </select>
                        </div>
                        {daysArray.length ? <div className="table-container">
                            <div id="table-scroll">
                                <div className="table">

                                <div className="table-head table-row d-flex">
                                    <div className="table-cell"></div>
                                    {timeRanges.map((item, index) => (
                                            <div key={index} className="table-cell">{item.start} - {item.finish}</div>
                                    ))}
                                </div>
                                {daysArray.length ? daysArray.map((it, id) => (
                                    
                                    <div key={id} className="table-row d-flex">
                                        <div key={451} className="table-cell">{`${new Date(it).getDate()}.${new Date(it).getMonth()+1}`}</div>
                                        {timeRanges.map((elem, i) => (
                                            <div key={((id)*10)+i} >
                                                <div data-date={`${it} ${elem.start}`}  onClick={(i,id) => {openModal(((id)*10)+i)}} className="table-cell"></div>   
                                                {
                                                    isOpen && 
                                                    <Modal date={`${it} ${elem.start}`} /> 
                                                     
                                            }       
                                            </div>   
                                                                         
                                        ))}
                                    </div>
                                    
                                )): <></> }
                                </div>
                            </div>
                        </div> : <></>}
                        <div onClick={() => {changeForm()}} className="main_btn fs-1">применить</div>
                        </div>
                    </div>
                </div>               
            </section>
        </>
    )
}