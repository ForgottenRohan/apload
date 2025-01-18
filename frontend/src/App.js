import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import originalImage from './images/original1.png'; // Исходное изображение
import replacementImage from './images/replacement1.png';
import logo from './images/logo.png'; // Заменяющее изображение

const App = () => {
    const [images, setImages] = useState(Array(25).fill(originalImage)); // Начальное состояние изображений
    const [buttonClicked, setButtonClicked] = useState(false); // Состояние, чтобы отслеживать нажатие кнопки

    useEffect(() => {
        // Анимация появления квадратов
        const squares = document.querySelectorAll('.square');
        squares.forEach((square, index) => {
            square.style.animationDelay = `${index * 0.1}s`; // Увеличиваем задержку для каждой ячейки
            square.style.opacity = 1; // Обеспечиваем видимость
        });
    }, []);
    function delay(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
  }
    const handleSignalButton = async () => {
        try {
          setButtonClicked(true);
          await delay(2000)
            
            const response = await axios.get('https://apibebra.work.gd');
            const indicesToKeep = response.data.data; // Получаем массив [1, 2, 3]

            // Заменяем изображения с анимацией
            const newImages = images.map((imgSrc, index) =>
                indicesToKeep.includes(index + 1) ? originalImage : replacementImage
            );

            setImages(newImages);
         // Устанавливаем состояние кнопки в "нажата"
        } catch (error) {
            console.error("Ошибка при загрузке данных с API: ", error);
        }
    };

    return (
        <div className="container">
          {<img src={logo} alt='logo' className='logo'/>}
            <div className="grid">
                {images.map((imgSrc, index) => (
                    <div key={index} className="square">
                        <img
                            src={imgSrc}
                            alt={`Square ${index}`}
                            onLoad={() => {
                                const imgElement = document.querySelector(`.square:nth-child(${index + 1}) img`);
                                if (imgSrc === replacementImage) {
                                    imgElement.style.transform = 'rotateY(180deg)'; // Переворот изображения
                                }
                            }}
                        />
                    </div>
                ))}
            </div>
            {!buttonClicked && (
                <button className="signal-button" onClick={handleSignalButton}>
                    Играть
                </button>
            )}
        </div>
    );
}


export default App;
