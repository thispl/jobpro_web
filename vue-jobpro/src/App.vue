<template>
  <!-- <div class="m-5">
    <Home_guest />
  </div>
    <div v-show="showNav">
      <Home_user />
    </div>
    <div>
      <Home_banner />
    </div>
    <div>
      <Home_category />
    </div> -->
    <div>
      <Home_jobs />
    </div>
</template>

<script setup>
  import { ref } from 'vue'
  import Home_guest from "./Home_guest.vue"
  import Home_user from "./Home_user.vue"
  import Home_banner from "./Home_banner.vue"
  import Home_category from "./Home_category.vue"
  import Home_jobs from "./Home_jobs.vue"
  
  const showNav = ref(false)

</script>




<!-- <template>
  <div class="m-6">
    <Button @click="todoList.fetch()">Show Todos</Button>
    <LoadingText v-if="todoList.list.loading" />
  </div>
  <div v-if="todoList.data">  
    <ul class="m-3 font-semibold text-blue-900" >
      <li v-for="todo in todoList.data">
        <div v-html="todo.designation"></div>
      </li>
    </ul>
  </div>
</template>

<script setup>

import { LoadingText, Button } from 'frappe-ui';
import { createListResource } from 'frappe-ui';

const todoList = createListResource({
  doctype: "Jobs",
  fields: ["designation", "description"]
})
console.log(todoList.data)

</script> -->