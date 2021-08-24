const App = {
    data() {
        return {
            counter: 0,
            sum: '123 UZS',
            url_rooms: 'http://127.0.0.1:8000/getrooms',
            url_hotels: 'http://127.0.0.1:8000/gethotels',
            rooms: [],
        }
    },
    delimiters: ["${", "}$"],
    methods:
    {
        get_rooms() {
            axios.get(this.url_rooms).then(response => {
                console.log(response.data)
            })
        },
        get_hotels() {
            axios.get(this.url_hotels).then(response => {
                console.log(response.data)
            })
        },

    },
    mounted() {
        axios.get(this.url_rooms).then(response => {
            console.log(response.data)
            this.rooms = response.data
        }),

        axios.get(this.url_hotels).then(response => {
            console.log(response.data)
            this.hotels = response.data
        })

    }

}

Vue.createApp(App).mount('#container')
