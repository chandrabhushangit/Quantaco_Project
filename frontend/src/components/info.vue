

<template>
<div v-if="true" class="modal-mask">
          <div class="relative max-h-full w-full max-w-md p-4 ml-[30%] mt-[10%]">
              <div class="modal-container bg-white rounded-lg shadow-md">
                  <div class="p-4 text-center md:p-5">
                        <svg class="mx-auto mb-4 w-20 text-blue-500 dark:text-blue-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" fill="none" />
                        <line x1="12" y1="16" x2="12" y2="12" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" />
                        <line x1="12" y1="8" x2="12" y2="8" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" />
                        </svg>

                      <!-- <h3 class=" text-lg font-normal text-gray-500 dark:text-gray-400">Please Fill all the mandatory Fields</h3>
                      <p class="mb-5"><span class="text-red-500">* </span>indicated Fields are mandatory</p> -->
                      <slot name="message">

                      </slot>
                      <button @click="$emit('closePopUp')" data-modal-hide="popup-modal" type="button" class="font-sm transform rounded bg-[#e1567c] px-4 py-2 text-white transition-transform duration-300 hover:scale-110 hover:bg-[#e1567c]">
                          Ok
                      </button>
                  </div>
              </div>
          </div>
      </div>
</template>

<style scoped>
.slide-fade-enter-active {
      transition: all 0.5s ease-out;
    }

.slide-fade-enter-from,
.slide-fade-leave-to {
      transform: translateX(20px);
      opacity: 0;
    }
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}
.modal-container {
  max-width: 100%;
  width: auto;
  max-height: 100%;
  overflow-y: auto;
  margin: auto;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.4s ease;
}
</style>