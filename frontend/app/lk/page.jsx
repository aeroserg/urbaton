'use client'

import { getCookie, deleteCookie } from 'cookies-next';
import Header from '../components/header';

export default function Lk(){
    const token = getCookie('XToken')
    console.log(getCookie('XToken'))
    return (
        <><Header isForLk={true}/></>
    )
}