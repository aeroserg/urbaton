import Header from "../../components/header"

export default function DetailPage({params: {id:id}}) {
    return (
        <>
        <Header />
        <section className="l-section">
            <div className="container-lg">
                <h1>Страница в разработке:(</h1>
                <p>Скоро здесь будет страница детаельной новости с динамическим id {id}</p>
            </div>
        </section>
          
        </>
    )
}