import Header from "./header"
import TimeTable from "./timetable"


export default function LkForParent(){
    return(
        <>
            <Header isForLk={'stud'} />
            <TimeTable isEditable={false} />
        </>
    )
}