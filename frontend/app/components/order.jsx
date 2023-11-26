'use client'

import { useEffect, useState } from "react"
import { getCookie } from "cookies-next"

export default function Orders() {
    const [orders,setOrders] = useState({
        orders:[]
    })

    useEffect(() => {
        if (getCookie('XToken')) {
            fetch('http://localhost/api/orders', {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${getCookie('XToken')}`
                  }
            })
            .then(response => response.json())
            .then(data =>{
                setOrders(data)
            })
        } 
    }, [])
    return (
        <>
            <section className="l-section">
                <div className="container-lg">
                    <div className="b_title">Заявки</div>
                    {orders.orders.length && <>
                        <div className="list">
                            {orders.orders.map((el,i) => (
                                <div key={el.id} className="listItem d-flex align-items-center">
                                    <div className="itemLeft">Заявка {el.id}</div>
                                    <div className="itemRight">
                                        <div className="itemSub itemSubTitle">{el.first_name} {el.last_name}</div>
                                        <div className="itemSub">{el.email}, {el.phone_number}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </>}
                </div>
            </section>
        </>
    )

}
