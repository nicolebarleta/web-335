const nodeShopper_customer = {

    customer: [
        {
            _id:"101",
            first_name: "Nicole",
            last_name: "Barleta",
            date_of_birth: "12/04/1992",
            user_name: "nicolebarleta"


        }
    ],

        invoice: [
            {
                _id:"invoice01",
                customer_id: "101",
                date_created:"10/10/2020",
                data_shipped:"10/11/2020",
                subtotal: 200,
                tax: 20.20,
                total: 220.20
            },
           
            {
                _id:"invoice02",
                customer_id: "101",
                date_created: "10/21/2020",
                data_shipped:"10/23/2020",
                subtotal: 99,
                tax: 30,
                total: 129
        
                    }
                ]
           
}