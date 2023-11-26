'use client'

import Header from "./header"
import Messages from "./messages"
import TimeTable from "./timetable"
import Order from "./order"

export default function LkForAdmin(){
  
    return(
        <>
            <Header isForLk={'school'} />
            <TimeTable isEditable={true} />
            <Messages />
            <Order />
        </>
    )
}