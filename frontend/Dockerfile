FROM node:alpine AS app
WORKDIR /app
COPY package.json package.json
RUN npm install
COPY . .
RUN npm run build
CMD [ "npm", "start" ]
# FROM nginx:stable-alpine
# COPY --from=app /app/public /usr/share/nginx/html
# COPY --from=app /app/nginx.conf /etc/nginx/conf.d/default.conf
# EXPOSE 3000
# CMD [ "nginx", "-g", "daemon off;" ]