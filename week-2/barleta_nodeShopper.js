const nodeShopper_details = {

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
            }
            ],

            line_items: [
                 {
                    _id: "item01",
                    invoice_id: "invoice01",
                    name: "pink chair",
                    price: 100,
                    quantity: 1
                 }
                ,

           
                {
                     _id: "item02",
                     invoice_id: "invoice01",
                     name: "red chair",
                    price: 100,
                    quantity: 1
                }
                   ],

        invoice: [
                    {
                        _id:"invoice02",
                        customer_id: "101",
                        date_created: "10/21/2020",
                        data_shipped:"10/23/2020",
                        subtotal: 99,
                        tax: 30,
                        total: 129
        
                    }
                    ],
        
            line_items: [
                         {
                            _id:"item03",
                            invoice_id: "invoice02",
                            name: "sugarcubs",
                            price: 99,
                            quantity: 1
                         }
                        ],



}