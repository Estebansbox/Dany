from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

router = APIRouter()

# Modelos de datos
class CrearCitaRequest(BaseModel):
    fecha: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}")
    hora_inicio: str = Field(..., pattern=r"\d{2}:\d{2}")
    nombre_paciente: str
    celular_contacto: str
    motivo_consulta: str

# Endpoints
@router.post("/crear_cita")
async def crear_cita(data: CrearCitaRequest):
    try:
        # Cálculo de fecha y hora final
        fecha_inicio = data.fecha
        hora_inicio = datetime.strptime(data.hora_inicio, "%H:%M")
        hora_fin = (hora_inicio + timedelta(minutes=45)).strftime("%H:%M")
        fecha_fin = fecha_inicio

        # Crear la respuesta para Make
        response = {
            "fecha_inicio": fecha_inicio,
            "hora_inicio": data.hora_inicio,
            "fecha_fin": fecha_fin,
            "hora_fin": hora_fin,
            "nombre_paciente": data.nombre_paciente,
            "celular_contacto": data.celular_contacto,
            "motivo_consulta": data.motivo_consulta,
        }

        return {"mensaje": "Datos calculados correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la cita: {e}")


@router.get("/buscar_cita")
async def buscar_cita(nombre_paciente: str, celular_contacto: str):
    try:
        # Simulación de respuesta desde Make (reemplazar con conexión real)
        response = {
            "mensaje": "Cita encontrada",
            "id": "cita123456",  # Ejemplo de ID
            "fecha": "2024-01-01",
            "hora_inicio": "10:00",
            "hora_fin": "10:45",
            "nombre_paciente": nombre_paciente,
            "celular_contacto": celular_contacto,
            "motivo_consulta": "Consulta de rutina"
        }

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar la cita: {e}")


@router.put("/editar_cita")
async def editar_cita(id_cita: str, nueva_fecha: str, nuevo_horario: str):
    try:
        # Cálculo de la nueva hora final
        nuevo_horario_inicio = datetime.strptime(nuevo_horario, "%H:%M")
        nuevo_horario_fin = (nuevo_horario_inicio + timedelta(minutes=45)).strftime("%H:%M")
        nueva_fecha_final = nueva_fecha  # La fecha final es igual a la nueva fecha de inicio

        # Crear la respuesta para Make
        response = {
            "id_cita": id_cita,
            "nueva_fecha_inicio": nueva_fecha,
            "nuevo_horario_inicio": nuevo_horario,
            "nueva_fecha_final": nueva_fecha_final,
            "nuevo_horario_final": nuevo_horario_fin,
        }

        return {"mensaje": "Datos de edición calculados correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al editar la cita: {e}")


@router.delete("/borrar_cita")
async def borrar_cita(id_cita: str):
    try:
        # Crear la respuesta para Make
        response = {
            "id_cita": id_cita,
        }

        return {"mensaje": "Datos de eliminación calculados correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar la cita: {e}")
