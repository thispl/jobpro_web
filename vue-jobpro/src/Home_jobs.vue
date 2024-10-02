<template>
    <!-- Jobs of the day -->
    <div class="my-16">
        <div class="text-center">
            <h1 class="font-bold dark:text-gray-900 text-3xl font-sans mt-6">Jobs of the day</h1>
            <p class="m-3 text-sm text-gray-600 font-semibold">Search and connect with the right candidate faster</p>
        </div>
    </div>
    <!-- Jobs filter -->
    <div>
        <div class="flex flex-row gap-4 justify-center">
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Content Writer</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Finance</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Human Resource</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Management</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Market Research</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Marketing & Sale</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Retail & Products</p>
            </div>
            <div class="border w-auto flex flex-row rounded-md">
                <img src="https://i.ibb.co/35Kxs1Y/Cybersecurity-Illustration-removebg-preview.png" alt="job photo" width="30px" />
                <p class="p-3 text-xs text-gray-900 font-bold">Software</p>
            </div>
        </div>
    </div>
    <!-- Job cards -->
    <div class="grid grid-cols-4 m-14 gap-10 w-10/12 mx-auto">
        <div v-if="todoList.data">
            <div class="border rounded-md hover:bg-white transition-colors px-3" style="background-color: rgb(248 250 252);">
                <h1 class="pt-3 text-sm text-gray-900 font-bold">Figma Designer</h1>
                <div class="flex flex-row text-xs text-gray-600 font-semibold gap-2 pt-2">
                    <p>Full Time</p>
                    <p>Posted 2 days ago</p>
                </div>
                <p class="flex flex-row text-xs text-gray-800 font-semibold pt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint voluptate natus soluta facere, veniam consectetur</p>
                <div class="flex gap-1.5 my-6">
                    <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">App</p>
                    <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">Figma</p>
                    <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">PSD</p>
                </div>
                <div class="flex flex-row-reverse pr-6 mb-5">
                    <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-2 focus:outline-none focus:ring-blue-300 font-medium rounded-md text-xs px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-600 transition-transform flex flex-row">
                        <p>Apply Now</p>
                    </button>
                </div>
            </div>
        </div>
        
        
        
    </div>
    <div class="grid grid-cols-4 m-14 gap-10 w-10/12 mx-auto">
        <div class="border rounded-md hover:bg-white transition-colors px-3" style="background-color: rgb(248 250 252);">
            <h1 class="pt-3 text-sm text-gray-900 font-bold">Figma Designer</h1>
            <div class="flex flex-row text-xs text-gray-600 font-semibold gap-2 pt-2">
                <p>Full Time</p>
                <p>Posted 2 days ago</p>
            </div>
            <p class="flex flex-row text-xs text-gray-800 font-semibold pt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint voluptate natus soluta facere, veniam consectetur</p>
            <div class="flex gap-1.5 my-6">
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">App</p>
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">Figma</p>
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">PSD</p>
            </div>
            <div class="flex flex-row-reverse pr-6 mb-5">
                <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-2 focus:outline-none focus:ring-blue-300 font-medium rounded-md text-xs px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-600 transition-transform flex flex-row">
                    <p>Apply Now</p>
                </button>
            </div>
        </div>
        <div class="border rounded-md hover:bg-white transition-colors px-3" style="background-color: rgb(248 250 252);">
            <h1 class="pt-3 text-sm text-gray-900 font-bold">Figma Designer</h1>
            <div class="flex flex-row text-xs text-gray-600 font-semibold gap-2 pt-2">
                <p>Full Time</p>
                <p>Posted 2 days ago</p>
            </div>
            <p class="flex flex-row text-xs text-gray-800 font-semibold pt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint voluptate natus soluta facere, veniam consectetur</p>
            <div class="flex gap-1.5 my-6">
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">App</p>
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">Figma</p>
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">PSD</p>
            </div>
            <div class="flex flex-row-reverse pr-6 mb-5">
                <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-2 focus:outline-none focus:ring-blue-300 font-medium rounded-md text-xs px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-600 transition-transform flex flex-row">
                    <p>Apply Now</p>
                </button>
            </div>
        </div>
        <div class="border rounded-md hover:bg-white transition-colors px-3" style="background-color: rgb(248 250 252);">
            <h1 class="pt-3 text-sm text-gray-900 font-bold">Figma Designer</h1>
            <div class="flex flex-row text-xs text-gray-600 font-semibold gap-2 pt-2">
                <p>Full Time</p>
                <p>Posted 2 days ago</p>
            </div>
            <p class="flex flex-row text-xs text-gray-800 font-semibold pt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint voluptate natus soluta facere, veniam consectetur</p>
            <div class="flex gap-1.5 my-6">
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">Adobexd</p>
                <p class="border dark:bg-slate-200 rounded-md text-xs font-sans px-2 pb-0.5">Figma</p>
            </div>
            <div class="flex flex-row-reverse pr-6 mb-5">
                <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-2 focus:outline-none focus:ring-blue-300 font-medium rounded-md text-xs px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-600 transition-transform flex flex-row">
                    <p>Apply Now</p>
                </button>
            </div>
        </div>       
    </div>
</template>

<script>
</script>