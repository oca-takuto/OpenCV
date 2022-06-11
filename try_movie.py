{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7aa54d79",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "34e5a185",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cv2.VideoCapture"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = cv2.VideoCapture('./sample.mp4')\n",
    "type(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8124743a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isOpened()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "643d6388",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    ret, frame = data.read()\n",
    "    \n",
    "    if ret:\n",
    "        cv2.imshow('sample data', frame)\n",
    "        cv2.waitKey(1)\n",
    "    else:\n",
    "        data.set(cv2.CAP_PROP_POS_FRAMES, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "18a5268c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'cv2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mcv2\u001b[49m\u001b[38;5;241m.\u001b[39mdestroyWindow(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124msample data\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'cv2' is not defined"
     ]
    }
   ],
   "source": [
    "cv2.destroyWindow('sample data')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
