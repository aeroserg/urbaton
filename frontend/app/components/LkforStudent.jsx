import Header from "./header"
import TimeTable from "./timetable"


export default function LkForStudent(){
    return(
        <>
            <Header isForLk={'stud'} />
            <TimeTable isEditable={false} />
        </>
    )
}