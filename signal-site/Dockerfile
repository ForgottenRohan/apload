FROM node:alpine AS app
WORKDIR /app
COPY package.json package.json
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine
COPY --from=app /app/build /usr/share/nginx/html 
COPY --from=app /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY /etc/letsencrypt/live/getsignals.run.place/fullchain.pem /etc/nginx/ssl/live/getsignals.run.place/fullchain.pem
COPY /etc/letsencrypt/live/getsignals.run.place/privkey.pem /etc/nginx/ssl/live/getsignals.run.place/privkey.pem
EXPOSE 3000
CMD [ "nginx", "-g", "daemon off;" ]