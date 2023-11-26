'use client'

import Header from "./header"
import { useEffect, useState } from "react"
import { getCookie } from "cookies-next"
import Messages from "./messages"
import TimeTable from "./timetable"

export default function LkForTeacher(){


    return(
        <>
            <Header isForLk={'school'} />
                <Messages />
                <TimeTable isEditable={false}/>
        </>
    )
}