const app  = Vue.createApp(
{
  data() {
    return {
    listItems : null,
    message :"boooo"
    }
    
    },
       methods: {
    async getAllRecords() {
      this.listItems = null
    const res = await fetch("/get_all_records");
    const finalRes = await res.json();
    this.listItems = finalRes
    console.log(this.listItems)
    }
    },delimiters : ['[[',']]'],
   
    
  }

);

app.mount('#app')
  