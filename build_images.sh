rm fastDeploy.py
wget https://raw.githubusercontent.com/notAI-tech/fastDeploy/master/cli/fastDeploy.py

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-telugu"}'
docker commit temp notaitech/anuvaad:english-telugu
docker push notaitech/anuvaad:english-telugu

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-tamil"}'
docker commit temp notaitech/anuvaad:english-tamil
docker push notaitech/anuvaad:english-tamil

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-malayalam"}'
docker commit temp notaitech/anuvaad:english-malayalam
docker push notaitech/anuvaad:english-malayalam

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-kannada"}'
docker commit temp notaitech/anuvaad:english-kannada
docker push notaitech/anuvaad:english-kannada

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-marathi"}'
docker commit temp notaitech/anuvaad:english-marathi
docker push notaitech/anuvaad:english-marathi

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-hindi"}'
docker commit temp notaitech/anuvaad:english-hindi
docker push notaitech/anuvaad:english-hindi

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-bengali"}'
docker commit temp notaitech/anuvaad:english-bengali
docker push notaitech/anuvaad:english-bengali

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-punjabi"}'
docker commit temp notaitech/anuvaad:english-punjabi
docker push notaitech/anuvaad:english-punjabi

python3 fastDeploy.py --build temp --source_dir fastDeploy_recipes --verbose --base pyt_1_5_cpu --port 1238 --extra_config '{"MODEL_NAME": "english-gujarati"}'
docker commit temp notaitech/anuvaad:english-gujarati
docker push notaitech/anuvaad:english-gujarati

rm fastDeploy.py

