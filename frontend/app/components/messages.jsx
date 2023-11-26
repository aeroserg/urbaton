import { useEffect,useState } from "react"
import { getCookie } from "cookies-next"


export default function Messages() {
    const [people,setPeople] = useState([])
    const [userValue, setUserValue] = useState('Выберете')
    const [textMessagesValue, setTextMessagesValue] = useState('')
    const [idTo, setIdTo] = useState(0)
    useEffect(() => {
        const HOST = location.protocol + '//' + location.host
        if (getCookie('XToken')) {
            fetch(`${HOST}/api/get_all_users`, {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${getCookie('XToken')}`
                  }
            })
            .then(response => response.json())
            .then(data =>{
                setPeople(data.users)
            })
        } 
    },[])
    const handleSubmit = async (e) => {
        e.preventDefault();
        let elements = e.target.elements;
        for (var i = 0, len = elements.length; i < len; ++i) {
            elements[i].readOnly = true;
        }
        const HOST = location.protocol + '//' + location.host

        const urls = {
            order: `${HOST}/api/send_message`,
        }
        const dataToSend = {
            id_to: idTo,
            text: textMessagesValue
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
                alert('Успешно отправлено')
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
    return(
        <>
            <section className="l-section">
                <div className="container-lg">
                 <form onSubmit={(e) => handleSubmit(e)}>

                    <div className="b_title">Отправить Сообщение</div>
                    <select name="" id={idTo} value={userValue} onChange={(e) => {setUserValue(e.target.value); setIdTo(e.target.selectedOptions[0].attributes.id.value)}}>
                        {people.map((item,index) => (
                            <option key={index} id={item.id} value={`${item.first_name} ${item.last_name} (${item.role})`}>{`${item.first_name} ${item.last_name} (${item.role})`}</option>
                        ))}
                    </select>
                  
                    <textarea name="" id="" value={textMessagesValue} onChange={(e) => {setTextMessagesValue(e.target.value)}} placeholder="Сообщение"></textarea>
                    <button type="submit">Отправить</button>
                    </form>
                </div>
            </section>
        </>
    )
}