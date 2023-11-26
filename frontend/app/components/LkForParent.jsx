import Header from "./header"
import TimeTable from "./timetable"
import { useEffect } from "react"


export default function LkForParent(){

    useEffect(() => {
        
    })

    return(
        <>
            <Header isForLk={'stud'} />
            <TimeTable isEditable={false} />
            <section className="l-section"> 
                <div className="container-lg">
                    <div className="b_title">Электронный невник</div>
                    <div className="marksWrapper">
                        <div className="marksWrpaaer_row head_row">
                            <div className="leftSide_cell">Предмет</div>
                            <div className="rightSide_cell">Оценки</div>
                        </div>
                        <div className="marksWrpaaer_row">
                            <div className="leftSide_cell">Флейта</div>
                            <div className="rightSide_cell">
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                            </div>
                        </div>
                        <div className="marksWrpaaer_row">
                            <div className="leftSide_cell">Сольфеджио</div>
                            <div className="rightSide_cell">
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                            </div>
                        </div>
                        <div className="marksWrpaaer_row">
                            <div className="leftSide_cell">Хор</div>
                            <div className="rightSide_cell">
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                            </div>
                        </div>
                        <div className="marksWrpaaer_row">
                            <div className="leftSide_cell">Живопись</div>
                            <div className="rightSide_cell">
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                            </div>
                        </div>
                        <div className="marksWrpaaer_row">
                            <div className="leftSide_cell">Скульптура</div>
                            <div className="rightSide_cell">
                                <div className="mark five">5</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                                <div className="mark four">4</div>
                                <div className="mark three">3</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}