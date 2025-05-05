# Chest Motion Monitoring System

This project is a wearable system for **real-time chest motion monitoring** using inertial sensors (accelerometer and gyroscope) to measure respiratory behavior and breathing patterns.

---

## 📌 Project Highlights

- Designed a wearable device using **Arduino Nano 33 IoT**
- Captures 3D acceleration & gyroscopic data from chest during rest and walking
- Uses **signal processing** and **feature extraction** to analyze breathing patterns
- Real-time data visualization and monitoring via serial interface

---

## 🧠 Key Technologies

- Arduino IDE, C++ (for embedded firmware)
- Python (NumPy, Pandas, SciPy, matplotlib)
- Jupyter Notebooks for signal processing and visualization
- Serial communication for data transfer and monitoring

---

## 🧪 Folder Structure

```
ChestMotionMonitoring-ML/
├── README.md
├── LICENSE
├── .gitignore
├── data/                  # Raw & processed data
├── notebooks/             # Jupyter notebooks
├── firmware/              # Arduino code
├── scripts/               # Python scripts (cleaning, analysis, plotting)
├── references/            # Research papers
├── results/               # Visuals like plots and evaluation metrics
```

---

## ⚙️ Arduino Firmware

Located in `/firmware/accNgyroTesting.ino`
- Configures IMU
- Streams AccX, AccY, AccZ, Gyro data at 50Hz
- Uses serial output

---

## 🧹 Python Workflow

1. **Data Collection & Saving** (`scripts/serial_data_saver.py`)
2. **Data Cleaning** (`scripts/data_cleaning.py`)
3. **Feature Extraction** (`scripts/feature_extraction.py`)
   - Zero-crossing detection
   - Breathing rate estimation
4. **Filtering & Amplification**
5. **Signal Visualization** (`scripts/live_plot_serial.py`)
6. **Scenario-based Analysis**

---

## 📊 Results

- Breathing rate error: **9.8 %**
- Zero-crossing error: **5.4 %**
- Real-time plots visualize breathing cycles & motion:
  ![image](https://github.com/user-attachments/assets/c7b14020-bf3f-4883-bfb8-d6cbb6aa9cd1)


---

## 📚 Research References

This project references a range of scientific literature related to respiratory monitoring, wearable sensors, chest motion analysis, and biomedical signal processing:

- Shafiq, G., & Veluvolu, K. C. (2017). Multimodal chest surface motion data for respiratory and cardiovascular monitoring applications. *Scientific Data*, 4, 170052. [Link](https://www.nature.com/articles/sdata201752)
- Ali, M., Elsayed, A., Mendez, A., Savaria, Y., & Sawan, M. (2021). Contact and remote breathing rate monitoring techniques: A review. *IEEE Sensors Journal*, 21(13), 14569–14586. [Link](https://ieeexplore.ieee.org/document/9400856)
- De Fazio, R., Stabile, M., De Vittorio, M., Velázquez, R., & Visconti, P. (2021). An overview of wearable piezoresistive and inertial sensors for respiration rate monitoring. *Electronics*, 10(17), 2178. [Link](https://www.mdpi.com/2079-9292/10/17/2178)
- Cedar, S. H. (2018). Every breath you take: the process of breathing explained. *Nursing Times*, 114(1), 47–50. [Link](https://www.researchgate.net/publication/323006715_Every_breath_you_take)
- Bilston, L. E., & Gandevia, S. C. (2014). Biomechanical properties of the human upper airway and their effect on its behavior during breathing and in obstructive sleep apnea. *Journal of Applied Physiology*, 116(3), 314–324. [Link](https://pubmed.ncbi.nlm.nih.gov/23823151/)
- Anand, D., Sambyal, S. A., & Vaid, R. (2021). Triboelectric nanogenerators (TENG): Factors affecting its efficiency and applications. *Facta Universitatis, Series: Electronics and Energetics*, 34(2), 157–172. [Link](https://www.researchgate.net/publication/353289133_Triboelectric_nanogenerators_TENG_Factors_affecting_its_efficiency_and_applications)
- Arthittayapiwat, K., Pirompol, P., & Samanpiboon, P. (2019). Chest expansion measurement in 3-dimension by using accelerometers. *Engineering Journal*, 23(2), 71–84. [Link](https://engj.org/index.php/ej/article/view/2846)
- Cleveland Clinic. (2023). Spirometry. [Link](https://my.clevelandclinic.org/health/diagnostics/17833-spirometry)
- Respiratory Therapy Zone. (2023). Capnography: A Comprehensive Overview. [Link](https://www.respiratorytherapyzone.com/capnography/)
- Wiliam, D. (2006). The half-second delay: what follows? *Pedagogy, Culture & Society*, 14(1), 71–81. [Link](https://www.tandfonline.com/doi/abs/10.1080/14681360500487470)
- Guk, K., Han, G., Lim, J., Jeong, K., Kang, T., Lim, E.-K., & Jung, J. (2019). Evolution of wearable devices with real-time disease monitoring for personalized healthcare. *Nanomaterials*, 9(6), 813. [Link](https://www.mdpi.com/2079-4991/9/6/813)
- Nicolò, A., Massaroni, C., Schena, E., & Sacchetti, M. (2020). The importance of respiratory rate monitoring: From healthcare to sport and exercise. *Sensors*, 20(21), 6396. [Link](https://www.mdpi.com/1424-8220/20/21/6396)
- Iqbal, T., Elahi, A., Ganly, S., Wijns, W., & Shahzad, A. (2022). Photoplethysmography-based respiratory rate estimation algorithm for health monitoring applications. *Journal of Medical and Biological Engineering*, 42(2), 242–252. [Link](https://pubmed.ncbi.nlm.nih.gov/35535218/)
- Nakajima, K., Tamura, T., & Miike, H. (1996). Monitoring of heart and respiratory rates by photoplethysmography using a digital filtering technique. *Medical Engineering & Physics*, 18(5), 365–372. [Link](https://pubmed.ncbi.nlm.nih.gov/8818134/)
- Pereira, C. B., Yu, X., Czaplik, M., Rossaint, R., Blazek, V., & Leonhardt, S. (2015). Remote monitoring of breathing dynamics using infrared thermography. *Biomedical Optics Express*, 6(11), 4378–4394. [Link](https://pubmed.ncbi.nlm.nih.gov/26601003/)
- De la Fuente, C., Weinstein, A., Guzman-Venegas, R., Arenas, J., Cartes, J., Soto, M., & Carpes, F. P. (2019). Use of accelerometers for automatic regional chest movement recognition during tidal breathing in healthy subjects. *Journal of Electromyography and Kinesiology*, 47, 105–112. [Link](https://www.sciencedirect.com/science/article/pii/S1050641118302230)
